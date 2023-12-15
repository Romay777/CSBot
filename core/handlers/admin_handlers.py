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
async def reveal_admin_panel(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.menu(is_admin=True))
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
async def reveal_admin_panel(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.menu(is_admin=True))
    await state.set_state(StepsForm.ADMIN_GET_USER_FOR_BALANCE)


@router.message(StepsForm.ADMIN_GET_USER_FOR_BALANCE)
async def get_user_id_balance(msg: Message, state: FSMContext, request: Request):
    await state.clear()
    await msg.answer(f"User balance with id [{msg.text}] = <code>{await request.get_balance(int(msg.text))}</code>")


@router.message(F.text == "ban user")
async def reveal_admin_panel(msg: Message, state: FSMContext):
    await msg.answer("Enter user_id:", reply_markup=kb.menu(is_admin=True))
    await state.set_state(StepsForm.ADMIN_GET_USER_ID_FOR_BAN)
