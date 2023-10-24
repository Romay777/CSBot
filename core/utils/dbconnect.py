import asyncpg
from core.utils import dbqueries
import text

DEFAULT_PLAYERS = ['playerone', 'playertwo', 'playerthree', 'playerfour', 'playerfive']


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        await self.connector.execute(dbqueries.ADD_DATA, user_id, user_name)

    async def get_balance(self, user_id):
        return '{:,}'.format(int(await self.connector.fetchval(dbqueries.GET_USER_BALANCE, user_id))).replace(
            ',', "'")
        #  return await self.connector.fetchval(dbqueries.GET_USER_BALANCE, user_id)
        #  это если не  нужно сразу форматировать под ***'***'***

    async def get_avgskill(self, user_id):
        return await self.connector.fetchval(dbqueries.GET_USER_AVG_SKILL, user_id)

    async def get_user_team(self, user_id):
        team = ""
        team_data = await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)
        for player in DEFAULT_PLAYERS:
            player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_TEAM_DATA, team_data[player])
            players_info = (f"<b>{player_data['nickname']} [{player_data['role']}]</b> - "
                            f"""Цена: <b>${'{:,}'.format(int(player_data['price'])).replace(',',
                                                                                                        "'")}</b>"""
                            f"\nНавыки: <b>{player_data['skill']}</b>\n")
            team += players_info
        return text.user_players.format(user_team=team,
                                        teamskill=await self.connector.fetchval(dbqueries.GET_USER_AVG_SKILL, user_id))

    async def get_user_position_ids_only(self, user_id):
        return await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)

    async def get_user_team_nicknames(self, user_id):
        team = []
        team_data = await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)

        for pl in DEFAULT_PLAYERS:
            player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_NICK_PRICE, team_data[pl])
            player = f"""{player_data['nickname']} [""" + f"""{'{:,}'.format(int(player_data['price']) // 3)
                                                                        .replace(',',"'")}]"""
            # player += (" [" + '{:,}'.format(int(player_data['price']) // 3).replace(',', "'") + "]") хз чо это
            team.append(player)

        return team

    async def update_user_avgskill(self, user_id):
        skillsum = 0
        players_ids = await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)
        for i in range(5):
            skillsum += await self.connector.fetchval(dbqueries.GET_PLAYER_SKILL, players_ids[i])
        await self.connector.execute(dbqueries.USER_AVGSKILL_UPDATE, skillsum // 5, user_id)

    async def sell_player(self, user_id, nickname):
        player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_ID_PRICE_BY_NICKNAME, nickname)
        player_user_team_pos = await self.connector.fetchval(dbqueries.GET_USER_PLAYER_POSITION,
                                                             player_data['playerid'], user_id)
        if player_user_team_pos == "No match":
            return f"Игрок {nickname} не в вашей команде."

        new_balance = (await self.connector.fetchval(dbqueries.GET_USER_BALANCE, user_id) +
                       int(player_data['price']) // 3)
        query = f"UPDATE users SET {str(player_user_team_pos)} = 0 WHERE user_id = $1"

        await self.connector.execute(query, user_id)
        await self.connector.execute(dbqueries.USER_BALANCE_UPDATE, new_balance, user_id)
        await self.update_user_avgskill(user_id)
        return text.player_sold.format(player_name=nickname, user_balance='{:,}'.format(new_balance).replace(",", "'"),
                                       team_skill=await self.get_avgskill(user_id))

    async def buy_player(self, user_id, position, nickname):
        player_id = await self.connector.fetchval(dbqueries.GET_PLAYER_ID_BY_NICKNAME, nickname)
        if player_id is None:
            return text.player_doesnt_exist
        query = f"UPDATE users SET {position} = $1 where user_id = $2"
        new_balance = (await self.connector.fetchval(dbqueries.GET_USER_BALANCE, user_id) -
                       int(await self.connector.fetchval(dbqueries.GET_PLAYER_PRICE_BY_PLAYERID, player_id)))
        if new_balance < 0:
            return text.not_enough_money

        await self.connector.execute(query, player_id, user_id)
        await self.update_user_avgskill(user_id)
        await self.connector.execute(dbqueries.USER_BALANCE_UPDATE, new_balance,  user_id)
        return text.player_bought.format(player_name=nickname,
                                         user_balance='{:,}'.format(new_balance).replace(",", "'"),
                                         team_skill=await self.get_avgskill(user_id))

    async def get_all_players(self):
        players = []
        total = await self.connector.fetchval(dbqueries.GET_TOTAL_PLAYERS)

        for i in range(1, total):
            player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_LIST_DATA, i)
            players_info = (f"<code>{player_data['nickname']}</code> | "
                            f"<b>{player_data['team']}</b> | "
                            f"""Цена: <b>${'{:,}'.format(int(player_data['price'])).replace(',', "'")}</b>\n""")
            players.append(players_info)

        return "".join(players)

    async def get_player_id_by_nickname(self, nickname):
        return await self.connector.fetchval(dbqueries.GET_PLAYER_ID_BY_NICKNAME, nickname)
