from aiogram import types

from aiogram.dispatcher import FSMContext
from for_states import Currency, Analitics
import for_request
from loader import bot

from models import Money
from models import User

import keyboard


def _get_pre(line):
    return f"<pre>{line}</pre>"


def _checking_for_correct(checking):
    try:
        checking = float(checking)
        return True
    except:
        return False


async def analysis(message: types.Message):
    await message.answer("Меню аналитики 🧮", reply_markup=keyboard.buttons_analysis())


async def common_information(message: types.Message):
    if Money.checking_null(message.from_user.id):
        await message.answer(_get_pre(Money.get_sum_money_str(message.from_user.id)), parse_mode=types.ParseMode.HTML)
    else:
        await message.answer("У вас еще нет ни одной записи")


async def get_curr(message: types.Message):
    rub = for_request.get_rate(456)
    eur = for_request.get_rate(451)
    usd = for_request.get_rate()
    await message.answer(f"Курс по НБРБ на сегодня:\n\n"
                         f"RUB  :  {rub}\n"
                         f"USD  :  {usd}\n"
                         f"EUR  :  {eur}")


async def main_menu(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Вернул", reply_markup=keyboard.buttons_start())


async def do_write(message: types.Message):
    if message.text != "Вернуться":
        if message.chat.type == "private":
            await message.answer('Выберите о какой валюте вы хотите сделать запись:',
                                 reply_markup=keyboard.buttons_currency())
    else:
        await message.answer(message.text, reply_markup=keyboard.buttons_start())


async def write_BYN(message: types.Message, state: FSMContext):
    if message.text != "Вернуться":
        if message.chat.type == "private":
            await state.update_data(state_run=message.text)
            await message.answer("Введи сумму в BYN", reply_markup=keyboard.buttons_currency_redaction())
            await Currency.state_1.set()
    else:
        await state.finish()
        await message.answer(message.text, reply_markup=keyboard.buttons_start())


async def write_two_curr(message: types.Message, state: FSMContext):
    if message.text != "Вернуться":
        answer = message.text
        if _checking_for_correct(answer):
            if message.chat.type == "private":
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
        else:
            await state.finish()
            await message.answer("Неверный формат данных", reply_markup=keyboard.buttons_currency())

    else:
        await state.finish()
        await message.answer(message.text, reply_markup=keyboard.buttons_start())


async def answer_curr(message: types.Message, state: FSMContext):
    if message.text != "Вернуться":
        answer = message.text
        if _checking_for_correct(answer):
            await state.update_data(state_2=answer)
            data = await state.get_data()
            byn = float(data.get('state_1'))
            two = float(data.get('state_2'))
            tempCurr = await state.get_data()
            tempCurr = tempCurr.get('state_run')
            tmoney = Money()
            if tempCurr == "USD":
                tmoney.set_money(BYN=byn, USD=two)
            elif tempCurr == "EUR":
                tmoney.set_money(BYN=byn, EUR=two)
            elif tempCurr == "RUB":
                tmoney.set_money(BYN=byn, RUB=two)
            Money.add_money(user_id=message.from_user.id, money=tmoney)
            a = byn / two
            result_str = f"Вы купили {two} {tempCurr} за {byn} BYN, курс покупки: " + "{:.5f}".format(
                a) + "\n" + f'Всего записей: {len(Money.get_monet_from_db(message.from_user.id))}'
            await message.answer(
                result_str,
                reply_markup=keyboard.buttons_currency())
            await state.finish()
        else:
            await state.finish()
            await message.answer("Неверный формат данных", reply_markup=keyboard.buttons_currency())
    else:
        await state.finish()
        await message.answer(message.text, reply_markup=keyboard.buttons_start())


async def hello(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"Привет {message.from_user.first_name}", reply_markup=keyboard.buttons_start())


async def start(message: types.Message):
    if message.chat.type == "private":
        welcom = "Этот бот создан для облегчения ведения учета покупок валюты " \
                 "он умеет хранить и обрабатывать информацию об этих покупках.\n" \
                 "Сейчас доступно 3 валюты для записи: RUB, USD, EUR.\n\n"
        current_user = User(message.from_user)
        if not User.check_unique(current_user.id):
            print(f"Новый юзер '{message.from_user.id}' '{message.from_user.username}'")
            User.write_to_DB(current_user)
            welcom = f"Приветствую тебя {message.from_user.first_name}, в ряду новых пользователей)\n\n" + welcom
        if Money.checking_null(message.from_user.id):
            welcom += "Для удаления записей введите комманду /delete"
    await message.answer(welcom, reply_markup=keyboard.buttons_start())


# async def information_about_writes(message: types.Message):
#     if message.chat.type == "private":
#         await message.answer(message.from_user.id, reply_markup=keyboard.button_information_writes())

async def list_writes(message: types.Message):
    if Money.checking_null(message.from_user.id):
        await message.answer(_get_pre(Money.get_list_writes_str(message.from_user.id)),
                             parse_mode=types.ParseMode.HTML)
    else:
        await message.answer("У вас еще нет ни одной записи")





async def show_button_delete_writes(callback_query: types.CallbackQuery):
    if Money.checking_null(callback_query.from_user.id):
        await bot.send_message(callback_query.from_user.id, "Сделайте выбор:\n",
                           reply_markup=keyboard.button_delete_writes_user())


async def delete_writes(callback_query: types.CallbackQuery):
    if Money.checking_null(callback_query.from_user.id):
        Money.delete_all_writes_about_money(callback_query.from_user.id)
        await bot.answer_callback_query(
            callback_query.id,
            text='Все записи удалены', show_alert=True)


async def cancel_delete(callback_query: types.CallbackQuery):
    if Money.checking_null(callback_query.from_user.id):
        message = callback_query.message
        await bot.delete_message(message.chat.id, message.message_id)
