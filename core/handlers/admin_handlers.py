from aiogram import F, Router
from aiogram.types import Message

from core.keyboards import kb
from core.middlewares.config import ADMIN_ID

router = Router()
router.message.filter(
    F.from_user.id == ADMIN_ID
)


@router.message(F.text == "admin")
async def reveal_admin_panel(msg: Message):
    await msg.answer("[admin panel revealed]", reply_markup=kb.admin_panel())

