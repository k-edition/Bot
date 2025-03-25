from aiogram import Bot, Dispatcher  # классы Bot и Dispatcher из основного модуля библиотеки aiogram
import asyncio  # для асинхронного запуска бота
import logging  # для настройки логгирования
import asyncpg  # для подключения к БД
from core.settings import settings, param
from core.handlers.basic import router
from core.handlers.contact import router_contact
from core.handlers.callback import router_inline
from core.handlers.form import router_fsm
from core.middlewares.counter_middleware import CounterMiddleware
from core.middlewares.opening_hours import OpeningHoursMiddleware
from core.middlewares.db_middleware import DbSession
from core import admin


async def create_pool():
    return await asyncpg.pool.create_pool(user=param.db.user, password=param.db.password,
                                          database=param.db.database, host=param.db.host, port=param.db.port,
                                          command_timeout=param.db.command_timeout)  # создадим пул соединений с БД


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(settings.bots.bot_token)  # объект бота
    poll_connect = await create_pool()
    dp = Dispatcher()  # объект диспетчера

    dp.message.middleware.register(CounterMiddleware())  # регистрируем middleware
    dp.message.middleware.register(OpeningHoursMiddleware())  # внимание! бот работает только в рабочие часы
    # dp.update.middleware.register(OpeningHoursMiddleware2())  # внимание! бот работает только в рабочие часы
    dp.update.middleware.register(DbSession(poll_connect))

    dp.include_router(router)  # регистрируем роутеры
    dp.include_router(router_contact)
    dp.include_router(router_inline)
    dp.include_router(router_fsm)

    @dp.startup()  # регистрация функции, которая вызывается при статрте бота
    async def on_startup():
        await admin.start_bot(bot)

    @dp.shutdown()  # регистрация функции, которая вызывается при остановке бота
    async def on_shutdown():
        await admin.stop_bot(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
