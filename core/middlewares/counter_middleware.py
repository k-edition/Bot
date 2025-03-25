from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable
from aiogram.types import Message


class CounterMiddleware(BaseMiddleware):  # добавляет в хендлер счетчик количества поступающих сообщений
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        return await handler(event, data)
