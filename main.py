import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.engine import URL

import config
from handlers import router
from db import BaseModel, create_async_engine, get_session_maker, proceed_schemas


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username="postgres",
        host="localhost",
        database="csbotdata",
        port=5432

    )

    async_engine = create_async_engine()
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
