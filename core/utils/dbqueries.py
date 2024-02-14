ADD_DATA = ("INSERT INTO users (user_id, user_name) "
            "VALUES ($1, $2) ON CONFLICT (user_id) DO UPDATE SET user_name = $2")

ADMIN_BAN_USER = """INSERT INTO banned_users (user_id, user_name, purpose) SELECT user_id, user_name, $2 FROM users 
                        WHERE user_id = $1 ON CONFLICT DO UPDATE SET purpose = excluded.purpose"""
ADMIN_UNBAN_USER = "DELETE FROM banned_users WHERE user_id = $1"
ADMIN_GET_USER_ID = "SELECT user_id FROM users WHERE LOWER(user_name) = LOWER($1)"

GET_USER_TEAM = "SELECT playerone, playertwo, playerthree, playerfour, playerfive FROM users WHERE user_id = $1"
GET_USER_BALANCE = "SELECT balance FROM users WHERE user_id = $1"
GET_USER_TEAM_ALL_SKILL = "SELECT sum(skill) FROM players WHERE playerid in ($1, $2, $3, $4, $5)"
GET_USER_TEAM_NICKS_PRICES = """SELECT price, nickname FROM players 
                                JOIN (VALUES ($1), ($2), ($3), ($4), ($5)) AS ids (playerid) 
                                ON players.playerid = ids.playerid;"""
GET_USER_AVG_SKILL_BY_USER_ID = "SELECT avgskill FROM users WHERE user_id = $1"
GET_USER_PLAYER_POSITION = """SELECT CASE WHEN playerone = $1 THEN 'playerone' WHEN playertwo = $1 THEN 'playertwo' 
                                WHEN playerthree = $1 THEN 'playerthree' WHEN playerfour = $1 THEN 'playerfour' WHEN playerfive = $1 THEN 'playerfive'
                                ELSE 'No match' END AS matched_column FROM users WHERE user_id = $2"""
GET_USER_TEAM_RANDOM_PLAYER_BY_USER_ID = """SELECT p.nickname FROM (SELECT CASE WHEN random_number < 0.2 THEN playerone
WHEN random_number < 0.4 THEN playertwo WHEN random_number < 0.6 THEN playerthree WHEN random_number < 0.8 THEN playerfour ELSE playerfive
END AS random_player FROM users, (SELECT RANDOM() AS random_number) AS subquery WHERE user_id = $1) 
AS u JOIN players p ON p.playerid = u.random_player;"""

GET_TOTAL_PLAYERS = "SELECT COUNT(*) FROM players"

GET_PLAYER_LIST_DATA = "SELECT nickname, team, price, skill FROM players WHERE playerid = $1"
GET_PLAYER_TEAM_DATA = "SELECT nickname, role, price, skill FROM players WHERE playerid = $1"

GET_PLAYER_ID_PRICE_BY_NICKNAME = "SELECT playerid, price FROM players WHERE nickname = $1"
GET_PLAYER_ID_BY_NICKNAME = "SELECT playerid FROM players WHERE LOWER(nickname) = LOWER($1)"
GET_PLAYER_PRICE_BY_PLAYERID = "SELECT price FROM players WHERE playerid = $1"
GET_PLAYER_NICK_PRICE = "SELECT price, nickname FROM players WHERE playerid = $1"
GET_PLAYER_SKILL = "SELECT skill FROM players WHERE playerid = $1"


USER_AVGSKILL_UPDATE = "UPDATE users SET avgskill = $1 where user_id = $2"
USER_BALANCE_UPDATE = "UPDATE users SET balance = $1 where user_id = $2"
USER_BALANCE_UPDATE_ADD = "UPDATE users SET balance = balance + $1 WHERE user_id = $2"
USER_BUY_SET_PLAYER = "UPDATE users SET $1 = $2 where user_id = $3"