from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message
from datetime import datetime


def hours() -> bool:
    return datetime.now().hour in ([i for i in range(8, 18)])


class TechnicalBreakUp(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        if hours():
            return await handler(event, data)

        await event.answer('Technical BreakUp')
