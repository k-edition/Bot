from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext  # 'этот класс отвечает за реализацию машины состояний
from core.utils.states_form import StepsForm  # класс состояний

router_fsm = Router()


@router_fsm.message(Command('form'))
async def get_form(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name}, начинаем заполнять анкету. Введите свое имя.")
    await state.set_state(StepsForm.GET_NAME)  # назначим пользователю состояние GET_NAME


@router_fsm.message(StepsForm.GET_NAME)
async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Твое имя: {message.text}\n"
                         f"Теперь введи фамилию.")
    await state.update_data(name=message.text)  # сохраним имя
    await state.set_state(StepsForm.GET_LAST_NAME)  # назначим пользователю состояние GET_LAST_NAME


@router_fsm.message(StepsForm.GET_LAST_NAME)
async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Твоя фамилия: {message.text}\n"
                         f"Теперь введи возраст.")
    await state.update_data(last_name=message.text)  # сохраним фамилию
    await state.set_state(StepsForm.GET_AGE)  # назначим пользователю состояние GET_AGE


@router_fsm.message(StepsForm.GET_AGE)
async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Твой возраст: {message.text}")
    context_data = await state.get_data()  # получим сохраненные в FSM данные
    await message.answer(f"Сохраненные данные:\n{str(context_data)}")  # отправим данные пользователю
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = (f"Вот твои данные:\nИмя: {name}\n"  # сформируем текст для сообщения
                 f"Фамилия: {last_name}\n"
                 f"Возраст: {message.text}")
    await message.answer(data_user)
    await state.clear()  # очистим машину состояний
