from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link

from core.keyboards import kb
from core.utils.dbconnect import Request
import text

router = Router()


@router.message(Command("start"))
async def get_start(msg: Message, request: Request):
    await request.add_data(msg.from_user.id, msg.from_user.first_name)
    await msg.answer(
        f"{hide_link('https://telegra.ph/file/65da62fba9401c09069c1.jpg')}"
        f"Привет, {html.bold(html.quote(msg.from_user.first_name))}!\n"
        f"Тебя приветствует игровой бот Counter-Strike! Здесь ты сможешь собрать свою команду.", reply_markup=kb.menu()
    )  # Для экранирования текст вынесен в хэндлер


@router.message(Command("globalelite"))
async def get_author(msg: Message):
    await msg.reply(text.author)


@router.message()  # Если не обработан ни один предыдущий хэндлер
async def answer_unknown_message(msg: Message):
    await msg.answer(text.unknown, reply_markup=kb.menu())
