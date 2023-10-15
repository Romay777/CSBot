ADD_DATA = ("INSERT INTO users (user_id, user_name) "
            "VALUES ($1, $2) ON CONFLICT (user_id) DO UPDATE SET user_name = $2")

GET_USER_TEAM = "SELECT playerone, playertwo, playerthree, playerfour, playerfive FROM users WHERE user_id = $1"
GET_USER_BALANCE = "SELECT balance FROM users WHERE user_id = $1"
GET_USER_AVG_SKILL = "SELECT avgskill FROM users WHERE user_id = $1"

GET_TOTAL_PLAYERS = "SELECT COUNT(*) FROM players"

GET_PLAYER_LIST_DATA = "SELECT nickname, team, price FROM players WHERE playerid = $1"
GET_PLAYER_TEAM_DATA = "SELECT nickname, role, price, skill FROM players WHERE playerid = $1"
GET_PLAYER_ID = "SELECT playerid FROM players WHERE nickname = $1"
GET_PLAYER_NICKNAME = "SELECT nickname FROM players WHERE playerid = $1"



