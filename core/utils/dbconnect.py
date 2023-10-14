import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        query = ("INSERT INTO users (user_id, user_name) "
                 "VALUES ($1, $2) ON CONFLICT (user_id) DO UPDATE SET user_name = $2")
        await self.connector.execute(query, user_id, user_name)

    async def get_balance(self, user_id):
        query = "SELECT balance FROM users WHERE user_id = $1"
        return str(await self.connector.fetchval(query, user_id))

    async def get_all_players(self):
        player = ''
        total = await self.connector.fetchval("SELECT COUNT(*) FROM players")
        for i in range(1, total):
            player += ("<code>" +
                       (await self.connector.fetchval("SELECT nickname from players where playerid = $1", i)
                        + "</code> \n"))
        return player
