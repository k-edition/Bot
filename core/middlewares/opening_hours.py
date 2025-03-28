from datetime import datetime
from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable
from aiogram.types import Message, TelegramObject


def opening_hours() -> bool:  # возвращает True, если текущее время рабочее
    return datetime.now().weekday() in (1, 2, 3, 4, 5) and datetime.now().hour in ([i for i in (range(8, 19))])


class OpeningHoursMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if not opening_hours():
            return await handler(event, data)
        await event.answer('Время работы бота:\n'
                           'Пн-пт с 8 до 18ч. Приходите в рабочие часы.')


class OpeningHoursMiddleware2(BaseMiddleware):  # второй вариант, отвечает на любое событие update
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if opening_hours():
            return await handler(event, data)
