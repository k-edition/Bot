from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='inline',
            description='Показать клавиатуру'
        ),
        BotCommand(
            command='form',
            description='Начать опрос'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
