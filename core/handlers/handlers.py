from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from core.keyboards import kb
import text

router = Router()


@router.message(F.text == "💸 Баланс")
async def get_balance(msg: Message):
    await msg.answer(text.balance, reply_markup=kb.menu)


@router.message(F.text == "💰 Купить/Продать игрока")
async def buy_sell_player(msg: Message):
    await msg.answer(text.choose_action.format(action="<b>[Покупка/Продажа]</b>"), reply_markup=kb.buy_sell_player)


@router.message(F.text == "🎮 Моя команда")
async def my_team(msg: Message):
    await msg.answer(text.user_players, reply_markup=kb.menu)


@router.message(F.text == "👤 Список игроков")
async def player_list(msg: Message):
    await msg.answer(text.player_list, reply_markup=kb.menu)


@router.message(F.text == "🤑 Фармить")
async def farming(msg: Message):
    await msg.answer(text.farm, reply_markup=kb.choose_farm)


@router.callback_query(F.data == "mac-10")
async def farm_mac10(callback: types.CallbackQuery):
    await callback.message.edit_text("mac-10 used", reply_markup=None)
    await callback.answer()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.menu)


@router.message(Command("globalelite"))
async def author(msg: Message):
    await msg.reply(text.author, reply_markup=kb.menu)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(text.unknown, reply_markup=kb.menu)
