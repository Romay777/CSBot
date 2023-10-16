ADD_DATA = ("INSERT INTO users (user_id, user_name) "
            "VALUES ($1, $2) ON CONFLICT (user_id) DO UPDATE SET user_name = $2")

GET_USER_TEAM = "SELECT playerone, playertwo, playerthree, playerfour, playerfive FROM users WHERE user_id = $1"
GET_USER_BALANCE = "SELECT balance FROM users WHERE user_id = $1"
GET_USER_AVG_SKILL = "SELECT avgskill FROM users WHERE user_id = $1"
GET_USER_PLAYER_POSITION = """SELECT CASE WHEN playerone = $1 THEN 'playerone' WHEN playertwo = $1 THEN 'playertwo' 
WHEN playerthree = $1 THEN 'playerthree' WHEN playerfour = $1 THEN 'playerfour' WHEN playerfive = $1 THEN 'playerfive'
ELSE 'No match' END AS matched_column FROM users WHERE user_id = $2"""

GET_TOTAL_PLAYERS = "SELECT COUNT(*) FROM players"

GET_PLAYER_LIST_DATA = "SELECT nickname, team, price FROM players WHERE playerid = $1"
GET_PLAYER_TEAM_DATA = "SELECT nickname, role, price, skill FROM players WHERE playerid = $1"

GET_PLAYER_ID_PRICE_BY_NICKNAME = "SELECT playerid, price FROM players WHERE nickname = $1"
GET_PLAYER_NICK_PRICE = "SELECT price, nickname FROM players WHERE playerid = $1"
GET_PLAYER_SKILL = "SELECT skill FROM players WHERE playerid = $1"


USER_AVGSKILL_UPDATE = "UPDATE users SET avgskill = $1 where user_id = $2"
USER_BALANCE_UPDATE = "UPDATE users SET balance = $1 where user_id = $2"