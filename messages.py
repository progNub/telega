from aiogram import types
from aiogram.dispatcher import FSMContext
from for_states import Currency

from models import User

import keyboard


async def analysis(message: types.Message):
    await message.answer("В процессе...")


async def return_main_menu(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        await state.finish()
        await message.answer(message.text, reply_markup=keyboard.buttons_start())


async def do_write(message):
    if message.chat.type == "private":
        await message.answer('Выберите о какой валюте вы хотите сделать запись:',
                             reply_markup=keyboard.buttons_currency())


async def write_BYN(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        await state.update_data(state_run=message.text)
        await message.answer("Введи сумму в BYN")
        await Currency.state_1.set()


async def write_two_curr(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        answer = message.text
        temp = await state.get_data()
        temp = temp.get('state_run')
        if temp == "USD":
            await state.update_data(state_1=answer)
            await message.answer("Введи сумму в USD")
            await Currency.state_2.set()
        elif temp == "EUR":
            await state.update_data(state_1=answer)
            await message.answer("Введи сумму в EUR")
            await Currency.state_2.set()
        elif temp == "RUB":
            await state.update_data(state_1=answer)
            await message.answer("Введи сумму в RUB")
            await Currency.state_2.set()
        else:
            await message.answer(f'Ошибка ввода данных, повторите попытку\nВведите сумму в{temp}')


async def answer_curr(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(state_2=answer)
    data = await state.get_data()
    BYN = data.get('state_1')
    TWO = data.get('state_2')
    print(BYN)
    print(TWO)
    await message.answer(f'ты ввел {TWO} = {BYN}')
    await state.finish()


async def hello(message):
    if message.chat.type == "private":
        await message.answer(f"Привет {message.from_user.first_name}")


async def start(message):
    if message.chat.type == "private":
        current_user = User(message.from_user)
        if not User.check_unique(current_user):
            User.write_to_json(current_user)
            User.write_to_DB(current_user)
            print(f"new user {message.from_user.user_name}")
        await message.answer(
            "Этот бот создается для удобства расчета покупок валюты, "
            "он может принимать записи и "
            "анализировать их", reply_markup=keyboard.buttons_start())
