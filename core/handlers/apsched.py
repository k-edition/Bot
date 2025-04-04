from aiogram import Bot
from core.settings import settings


async def send_message_time(bot: Bot):  # выполняется один раз в указанное время
    await bot.send_message(settings.bots.admin_id, f"через 30 секунд")


async def send_message_cron(bot: Bot):  # выполняется каждый день в одно и тоже время
    await bot.send_message(settings.bots.admin_id, f"ежедневно в одно и тоже время")


async def send_message_interval(bot: Bot):  # выполняется с определенным интервалом времени
    await bot.send_message(settings.bots.admin_id, f"с интервалом 3 минуты")


async def send_message_middleware(bot: Bot, chat_id:int):
    await bot.send_message(chat_id, f'сформировано middleware')  # добавлено в хендлер form.get_age
