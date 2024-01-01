from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NICKNAME = State()

    IS_PLAYING = State()

    ADMIN_GET_USER_FOR_BALANCE = State()
    ADMIN_GET_USER_ID_FOR_BAN_UNBAN = State()
    ADMIN_GET_USER_BALANCE_CHANGING = State()
