from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.utils.statesform import StepsForm
from core.utils.dbconnect import Request

from core.keyboards import kb
from core.middlewares.config import ADMIN_ID

router = Router()
router.message.filter(
    F.from_user.id == ADMIN_ID
)


@router.message(F.text == "admin")
async def reveal_admin_panel(msg: Message):
    await msg.answer("[admin panel revealed]", reply_markup=kb.menu(is_admin=True))


@router.message(F.text == "set user balance")
async def getting_user_id(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.back_button())
    await state.set_state(StepsForm.ADMIN_GET_USER_BALANCE_CHANGING)


@router.message(StepsForm.ADMIN_GET_USER_BALANCE_CHANGING)
async def get_user_id_balance(msg: Message, state: FSMContext, request: Request):
    if (await state.get_data()).get('target_user_id') is None:
        await state.update_data(target_user_id=msg.text)
        await msg.answer(f"Current balance = [{await request.get_balance(int(msg.text))}]\nEnter new balance:")
    else:
        await request.update_user_balance(int(msg.text), int((await state.get_data()).get('target_user_id')))
        await msg.answer("Balance updated successfully")
        await state.clear()


@router.message(F.text == "get user balance")
async def getting_user_id(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.back_button())
    await state.set_state(StepsForm.ADMIN_GET_USER_FOR_BALANCE)


@router.message(StepsForm.ADMIN_GET_USER_FOR_BALANCE)
async def get_user_balance_by_id(msg: Message, state: FSMContext, request: Request):
    await state.clear()
    await msg.answer(f"User balance with id [{msg.text}] = <code>{await request.get_balance(int(msg.text))}</code>",
                     reply_markup=kb.menu(is_admin=True))


@router.message(F.text == "ban user")
async def getting_id(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.back_button())
    await state.set_state(StepsForm.ADMIN_GET_USER_ID_FOR_BAN_UNBAN)
    await state.update_data(action="ban")


@router.message(F.text == "unban user")
async def getting_id(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.back_button())
    await state.set_state(StepsForm.ADMIN_GET_USER_ID_FOR_BAN_UNBAN)
    await state.update_data(action="unban")


@router.message(StepsForm.ADMIN_GET_USER_ID_FOR_BAN_UNBAN)
async def ban_unban_user_by_id(msg: Message, state: FSMContext, request: Request):
    action = (await state.get_data()).get('target_user_id')
    await state.clear()
    if action == "ban":
        await request.ban_user(int(msg.text))
        await msg.answer(f"User_id [{msg.text}] has been banned", reply_markup=kb.menu(is_admin=True))
    else:
        await request.unban_user(int(msg.text))
        await msg.answer(f"User_id [{msg.text}] has been unbanned", reply_markup=kb.menu(is_admin=True))


@router.message(F.text == "get tgid")
async def getting_tgid(msg: Message, state: FSMContext):
    await msg.answer("Enter user_name:", reply_markup=kb.back_button())
    await state.set_state(StepsForm.ADMIN_GET_USER_TGID)


@router.message(StepsForm.ADMIN_GET_USER_TGID)
async def get_tgid_by_user_name(msg: Message, state: FSMContext, request: Request):
    await state.clear()
    user_id = await request.get_tgid(msg.text)
    await msg.answer(str(user_id), reply_markup=kb.menu(is_admin=True))
