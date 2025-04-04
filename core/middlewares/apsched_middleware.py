from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable
from aiogram.types import TelegramObject
from apscheduler.schedulers.asyncio import AsyncIOScheduler  # планировщик задач


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler) -> None:
        self.scheduler = scheduler

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data['apscheduler'] = self.scheduler  # в словарь с данными хендлера добавляем объект apscheduler
        return await handler(event, data)  # обновлям данные в хендлере
