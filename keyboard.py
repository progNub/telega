from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# def buttons_analysis():
#     btn1 = KeyboardButton('Общая информация')
#     btn2 = KeyboardButton('Выбрать валюту')
#     btn3 = KeyboardButton('Курсы валют')
#     btn4 = KeyboardButton("Вернуться")
#     keys = ReplyKeyboardMarkup(resize_keyboard=True)
#     keys.add(btn1, btn2)
#     keys.add(btn3, btn4)
#     return keys


def buttons_start():
    btn1 = KeyboardButton('Привет! 👋')
    btn2 = KeyboardButton('Сделать запись ✍')
    btn3 = KeyboardButton('Аналитика 🧮')
    btn4 = KeyboardButton('Инструкция ❓')
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.add(btn1, btn2)
    keys.add(btn3, btn4)
    return keys


def buttons_currency():
    btn1 = KeyboardButton('USD')
    btn2 = KeyboardButton('EUR')
    btn3 = KeyboardButton('RUB')
    btn4 = KeyboardButton('Вернуться')
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.add(btn1, btn2)
    keys.add(btn3, btn4)
    return keys
