from aiogram import types, F, Router, html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.keyboards import kb, inline
from core.utils.dbconnect import Request
from core.utils.statesform import StepsForm
import text

router = Router()


@router.callback_query(F.data == "gun_choosed")
async def farm_gun_choosed(callback: types.CallbackQuery):
    await callback.message.edit_text(text.farm_choose_side, reply_markup=inline.choose_side_kb())
    await callback.answer()


@router.callback_query(F.data == "side_choosed")
async def play_side_a(callback: types.CallbackQuery, state: FSMContext, request: Request):
    if not "True" == (await state.get_data()).get('playing'):
        await state.set_state(StepsForm.IS_PLAYING)
        await state.update_data(playing="True")
        await callback.answer()
        await callback.message.edit_text(await request.farming(callback.from_user.id, callback))
        await state.clear()
    else:
        await callback.message.edit_text(text.farm_already_playing)


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
            break
    if not player_found:
        await message.answer(f"Запрос на покупку игрока {html.bold(html.quote(message.text))}...")
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
