from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME = State()  # создаем состояние "ожидание ввода имени"
    GET_LAST_NAME = State()  # создаем состояние "ожидание ввода фамилии"
    GET_AGE = State()  # создаем состояние "ожидание ввода возраста"
