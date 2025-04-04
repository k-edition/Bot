from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler  # планировщик задач
from core.handlers import apsched
from core.settings import settings
from core.utils.commands import set_commands
from datetime import datetime, timedelta

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')  # объект расписания


async def start_bot(bot: Bot):  # отправит уведомление админу о старте бота
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')

    scheduler.add_job(apsched.send_message_time, trigger='date',
                      run_date=datetime.now() + timedelta(seconds=30), kwargs={'bot': bot})

    scheduler.add_job(apsched.send_message_cron, trigger='cron',
                      hour=datetime.now().hour, minute=datetime.now().minute + 5,
                      start_date=datetime.now(), kwargs={'bot': bot})

    scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=180, kwargs={'bot': bot})

    scheduler.start()


async def stop_bot(bot: Bot):  # отправит уведомление админу об остановке бота
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')
    scheduler.shutdown(wait=False)  # wait=False предотвращает deadlock при завершении
