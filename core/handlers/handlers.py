from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.keyboards import kb, inline
from core.utils.dbconnect import Request
from core.utils.statesform import StepsForm
import text

router = Router()


@router.message(F.text == "💸 Баланс")
async def get_balance(msg: Message, request: Request):
    balance = await request.get_balance(user_id=msg.from_user.id)
    await msg.answer(text.balance.format(user_balance=balance),
                     reply_markup=kb.menu())


@router.message(F.text == "💰 Купить/Продать игрока")
async def buy_sell_player(msg: Message):
    await msg.answer(text.choose_action.format(action="<b>[Покупка/Продажа]</b>"), reply_markup=inline.buy_sell_kb())


@router.message(F.text == "🎮 Моя команда")
async def my_team(msg: Message, request: Request):
    await msg.answer(await request.get_user_team(msg.from_user.id), reply_markup=kb.menu())


@router.message(F.text == "👤 Список игроков")
async def player_list(msg: Message, request: Request):
    await msg.answer(await request.get_all_players(), reply_markup=kb.menu())


@router.message(F.text == "🤑 Фармить")
async def farming(msg: Message):
    await msg.answer(text.farm, reply_markup=inline.farm_methods_kb())


@router.callback_query(F.data == "buy_player")
async def buy_player_list_creation(callback: types.CallbackQuery, request: Request):
    positions = await request.get_user_position_ids_only(callback.from_user.id)
    await callback.message.edit_text("Выберите, на какую позицию хотите установить игрока:",
                                     reply_markup=inline.position_list(positions))
    await callback.answer()


@router.callback_query(F.data.startswith('buy_on_'))
async def buy_player_waiting_nickname(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Напишите никнейм игрока, которого хотите купить:\n"
                                     "<b>[Его можно скопировать нажатием из списка игроков]</b>")
    await callback.answer()
    # Вот тут машина состояний, ожидание никнейма.
    await state.set_state(StepsForm.GET_NICKNAME)
    await state.update_data(position=callback.data.replace("buy_on_", ""))


@router.message(StepsForm.GET_NICKNAME)
async def buy_player_nickname_got(message: Message, request: Request, state: FSMContext):
    position = (await state.get_data()).get('position')
    await state.clear()
    buying_player_id = await request.get_player_id_by_nickname(message.text)
    player_found = False
    for pl_id in await request.get_user_position_ids_only(message.from_user.id):
        if buying_player_id == pl_id:
            await message.answer("Данный игрок уже в вашей команде.")
            player_found = True
    if not player_found:
        await message.answer(f"Запрос на покупку игрока <b>{message.text}...</b>")
        await message.answer(await request.buy_player(message.from_user.id, position, message.text))


@router.callback_query(F.data == "sell_player")
async def sell_player_list_creation(callback: types.CallbackQuery, request: Request):
    await callback.message.edit_text(
        "Выберите игрока, которого хотите продать (указана сумма, которая вернется на баланс)",
        reply_markup=inline.get_nicknames_keyboard(await request.get_user_team_nicknames(callback.from_user.id)))
    await callback.answer()


@router.callback_query(F.data.startswith('sell_'))
async def selling_player(callback: types.CallbackQuery, request: Request):
    player_nickname = callback.data.replace("sell_", "").split()[0]
    await callback.message.edit_text(f"Продажа {player_nickname}...", reply_markup=None)
    await callback.answer()
    await callback.message.answer(await request.sell_player(user_id=callback.from_user.id, nickname=player_nickname),
                                  reply_markup=kb.menu())


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
    await callback.message.edit_text("mac-10 used", reply_markup=inline.choose_side_kb())
    await callback.answer()


@router.callback_query(F.data == "ump-45")
async def farm_ump_45(callback: types.CallbackQuery):
    await callback.message.edit_text("ump used", reply_markup=inline.choose_side_kb())
    await callback.answer()


@router.callback_query(F.data == "mp-7")
async def farm_mp_7(callback: types.CallbackQuery):
    await callback.message.edit_text("mp7 used", reply_markup=inline.choose_side_kb())
    await callback.answer()


@router.message(Command("start"))
async def get_start(msg: Message, request: Request):
    await request.add_data(msg.from_user.id, msg.from_user.first_name)
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.menu())


@router.message(Command("globalelite"))
async def author(msg: Message):
    await msg.reply(text.author, reply_markup=kb.menu())


@router.message()
async def message_handler(msg: Message):
    await msg.answer(text.unknown, reply_markup=kb.menu())
