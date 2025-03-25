from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsTrueContact(BaseFilter):  # кастомный фильтр, что пользователь отправил свой контакт
    async def __call__(self, message: Message):
        if message.contact and message.contact.user_id == message.from_user.id:
            return {'phone': message.contact.phone_number}
        return False
