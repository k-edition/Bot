from aiogram import Router
from aiogram.types import Message
from core.filters.is_contact import IsTrueContact

router_contact = Router()


@router_contact.message(IsTrueContact())
async def get_true_contact(message: Message, phone: str):  # если пользователь отправит свой контакт
    await message.answer(f"Ты отправил свой контакт {phone}.")


@router_contact.message(lambda message: message.contact is not None)
async def get_false_contact(message: Message):  # если пользователь отправит НЕ свой контакт
    await message.answer(f"Ты отправил не свой контакт.")
