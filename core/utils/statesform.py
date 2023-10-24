from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NICKNAME = State()
