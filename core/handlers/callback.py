from aiogram import Router
from aiogram.types import CallbackQuery
from core.utils.callback_data import MacInfo


router_inline = Router()


@router_inline.callback_query(MacInfo.filter())  # чтобы работали только кнопки с моделью pro укжем аргумент F.model == 'pro' в скобках
async def select_macbook(call: CallbackQuery, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    year = callback_data.year
    answer = f"Ты выбрал Macbook {model}, диагональ {size} {year} года."
    await call.message.answer(answer)
    await call.answer()
    