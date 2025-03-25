from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback_data import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Macbook',
                             callback_data='apple_air_13_2015')
    ],
    [
        InlineKeyboardButton(text='Macbook2',
                             callback_data='apple_pro_14_2020')
    ],
    [
        InlineKeyboardButton(text='Macbook3',
                             callback_data='apple_pro_16_2022')
    ],
    [
        InlineKeyboardButton(text='link',
                             url='https://ya.ru')
    ],
    [
        InlineKeyboardButton(text='profile',
                             url='tg://user?id=1602871707')
    ]

])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook', callback_data=MacInfo(model='air', size=13, year=2015))
    keyboard_builder.button(text='Macbook2', callback_data=MacInfo(model='pro', size=14, year=2020))
    keyboard_builder.button(text='Macbook3', callback_data=MacInfo(model='pro', size=16, year=2022))
    keyboard_builder.button(text='link', url='https://ya.ru')
    keyboard_builder.button(text='profile', url='tg://user?id=1602871707')
    keyboard_builder.adjust(3, 2)
    return keyboard_builder.as_markup()
