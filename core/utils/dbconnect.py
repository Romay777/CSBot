import asyncpg
from core.utils import dbqueries
import text


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        await self.connector.execute(dbqueries.ADD_DATA, user_id, user_name)

    async def get_balance(self, user_id):
        return await self.connector.fetchval(dbqueries.GET_USER_BALANCE, user_id)

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

    async def get_user_team(self, user_id):
        team = ""
        team_data = await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)
        players = ['playerone', 'playertwo', 'playerthree', 'playerfour', 'playerfive']
        for player in players:
            player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_TEAM_DATA, team_data[player])
            players_info = (f"<code>{player_data['nickname']}</code> <b>[{player_data['role']}]</b> - "
                            f"Его текущая цена: <b>${player_data['price']}</b>\n"
                            f"Его навыки: <b>{player_data['skill']}</b>\n")
            team += players_info
        return text.user_players.format(user_team=team,
                                        teamskill=await self.connector.fetchval(dbqueries.GET_USER_AVG_SKILL, user_id))

    async def get_user_team_nicknames(self, user_id, choosing=False):
        if not choosing:
            team = []
            team_data = await self.connector.fetchrow(dbqueries.GET_USER_TEAM, user_id)
            players = ['playerone', 'playertwo', 'playerthree', 'playerfour', 'playerfive']
            for pl in players:
                player_data = await self.connector.fetchrow(dbqueries.GET_PLAYER_NICK_PRICE, team_data[pl])
                player = player_data['nickname']
                player += (" [" + '{:,}'.format(int(player_data['price'])//3).replace(',', "'") + "]")
                team.append(player)
            return team
