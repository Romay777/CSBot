from aiogram import F, Router
from aiogram.types import Message

from core.keyboards import kb
import text

router = Router()
router.message.filter(
    F.from_user.id == 880825017
)


@router.message(F.text == "admin")
async def admin_panel(msg: Message):
    await msg.answer("[admin panel revealed]", reply_markup=kb.admin_panel())

