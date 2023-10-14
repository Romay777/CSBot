import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from core.handlers.handlers import router
from core.middlewares import config
from core.middlewares.technical_breakup import TechnicalBreakUp
from core.middlewares.dbmiddleware import DbSession
import asyncpg


async def create_pool():
    return await asyncpg.create_pool(user='postgres', database='csbotdata',
                                     host='localhost', port='5432',
                                     password='Ggwpggwp1')


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    pool_connect = await create_pool()
    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware.register(DbSession(pool_connect))
    dp.message.middleware.register(TechnicalBreakUp())
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
