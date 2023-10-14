from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from core.keyboards import kb, inline
from core.utils.dbconnect import Request
import text

router = Router()


@router.message(F.text == "💸 Баланс")
async def get_balance(msg: Message, request: Request):
    await msg.answer(text.balance.format(user_balance=await request.get_balance(user_id=msg.from_user.id)),
                     reply_markup=kb.menu_kb)


@router.message(F.text == "💰 Купить/Продать игрока")
async def buy_sell_player(msg: Message):
    await msg.answer(text.choose_action.format(action="<b>[Покупка/Продажа]</b>"), reply_markup=inline.buy_sell_kb)


@router.message(F.text == "🎮 Моя команда")
async def my_team(msg: Message):
    await msg.answer(text.user_players, reply_markup=kb.menu_kb)


@router.message(F.text == "👤 Список игроков")
async def player_list(msg: Message, request: Request):
    await msg.answer(str(await request.get_all_players()), reply_markup=kb.menu_kb)


@router.message(F.text == "🤑 Фармить")
async def farming(msg: Message):
    await msg.answer(text.farm, reply_markup=inline.farm_kb)


@router.callback_query(F.data == "buy_player")
async def play_side_a(callback: types.CallbackQuery):
    await callback.message.edit_text("buying", reply_markup=None)
    await callback.answer()


@router.callback_query(F.data == "sell_player")
async def play_side_a(callback: types.CallbackQuery):
    await callback.message.edit_text("selling", reply_markup=None)
    await callback.answer()


@router.callback_query(F.data == "side-a")
async def play_side_a(callback: types.CallbackQuery):
    await callback.message.edit_text("A side", reply_markup=None)
    await callback.answer()


@router.callback_query(F.data == "side-b")
async def play_side_b(callback: types.CallbackQuery):
    await callback.message.edit_text("B side", reply_markup=None)
    await callback.answer()


@router.callback_query(F.data == "mac-10")
async def farm_mac10(callback: types.CallbackQuery):
    await callback.message.edit_text("mac-10 used", reply_markup=inline.choose_side_kb)
    await callback.answer()


@router.callback_query(F.data == "ump-45")
async def farm_ump_45(callback: types.CallbackQuery):
    await callback.message.edit_text("ump used", reply_markup=inline.choose_side_kb)
    await callback.answer()


@router.callback_query(F.data == "mp-7")
async def farm_mp_7(callback: types.CallbackQuery):
    await callback.message.edit_text("mp7 used", reply_markup=inline.choose_side_kb)
    await callback.answer()


@router.message(Command("start"))
async def get_start(msg: Message, request: Request):
    await request.add_data(msg.from_user.id, msg.from_user.first_name)
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.menu_kb)


@router.message(Command("globalelite"))
async def author(msg: Message):
    await msg.reply(text.author, reply_markup=kb.menu_kb)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(text.unknown, reply_markup=kb.menu_kb)
