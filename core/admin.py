from aiogram import Bot
from core.settings import settings
from core.utils.commands import set_commands


async def start_bot(bot: Bot):  # отправит уведомление админу о старте бота
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):  # отправит уведомление админу об остановке бота
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')
