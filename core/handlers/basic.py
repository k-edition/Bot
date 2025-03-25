from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import json  # для сериализации message
import channels  # файл с участниками рассылки
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard
from core.utils.db_connect import Request

router = Router()


@router.message(Command('start'))
async def get_start(message: Message, counter: int, request: Request):  # ответ на команду /start
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f"Сообщение №{counter}")  # дополнительно отправляет номер сообщения
    await message.answer(f"{message.from_user.first_name}, чтобы забрать все полезные материалы"
                         f" из нашей рассылки, подпишись на всех организаторов:\n"
                         f"\n"
                         f"{channels.channel1}\n"
                         f"{channels.channel2}\n"
                         f"\n"
                         f"После подписки нажми ГОТОВО",
                         reply_markup=get_reply_keyboard())


@router.message(Command('inline'))  # ответ на команду /inline
async def get_inline(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}. Выбери кнопку",
                         reply_markup=get_inline_keyboard())


@router.message(F.photo)
async def get_photo(message: Message, bot: Bot):  # сохраним файл, отправленный юзером
    await message.answer(f"Ты отправил картинку, я сохраню ее себе")
    print(await bot.get_file(message.photo[-1].file_id))
    file = await bot.get_file(message.photo[-1].file_id)  # получаем объект file
    await bot.download_file(file.file_path, 'photo.jpg')  # сохраняем файл


@router.message(F.text.lower() == 'привет')  # ответ на текст 'Привет'
async def get_hello(message: Message):
    await message.answer(f"И тебе привет")
    json_str = json.dumps(message.dict(), default=str)  # сериализуем message в JSON-структуру
    print(json_str)


@router.message(lambda message: message.location is not None)  # в ответ на отправку геолокации
async def get_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(f"Ты отправил локацию!\r\a"
                         f"{latitude}\r\n{longitude}")
