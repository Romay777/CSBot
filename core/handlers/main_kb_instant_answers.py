from aiogram import F, Router
from aiogram.types import Message

from core.keyboards import inline
from core.utils.dbconnect import Request
import text

router = Router()


@router.message(F.text == "💸 Баланс")
async def get_balance(msg: Message, request: Request):
    await msg.answer(text.balance.format(user_balance=await request.get_balance(user_id=msg.from_user.id)))


@router.message(F.text == "🤑 Фармить")
async def start_farming(msg: Message):
    await msg.answer(text.farm_choose_method, reply_markup=await inline.get_farm_methods())


@router.message(F.text == "💰 Купить/Продать игрока")
async def buy_sell_player(msg: Message):
    await msg.answer(text.choose_action.format(action="<b>[Покупка/Продажа]</b>"), reply_markup=await inline.get_buy_sell_kb())


@router.message(F.text == "🎮 Моя команда")
async def my_team_reveal(msg: Message, request: Request):
    await msg.answer(await request.get_user_team(msg.from_user.id))


@router.message(F.text == "👤 Список игроков")
async def player_list_reveal(msg: Message, request: Request):
    await msg.answer(await request.get_all_players())
