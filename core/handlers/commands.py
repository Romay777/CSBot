from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from core.keyboards import kb
from core.utils.dbconnect import Request
import text

router = Router()


@router.message(Command("start"))
async def get_start(msg: Message, request: Request):
    await request.add_data(msg.from_user.id, msg.from_user.first_name)
    await msg.answer(text.greet.format(name=msg.from_user.first_name), reply_markup=kb.menu())


@router.message(Command("globalelite"))
async def author(msg: Message):
    await msg.reply(text.author)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(text.unknown, reply_markup=kb.menu())
