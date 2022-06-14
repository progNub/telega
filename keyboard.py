from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



def buttons_analysis():
    btn1 = KeyboardButton('Общая информация')
    btn2 = KeyboardButton('Список записей')
    btn3 = KeyboardButton('Курсы валют')
    btn4 = KeyboardButton("Вернуться")
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.add(btn1, btn2)
    keys.add(btn3, btn4)
    return keys


# def button_information_writes():
#     btn1 = KeyboardButton('Список всех записей')
#     btn2 = KeyboardButton('Изменить запись')
#     btn3 = KeyboardButton('Удалить')
#     btn4 = KeyboardButton("Вернуться в предыдущее меню")
#     keys = ReplyKeyboardMarkup(resize_keyboard=True)
#     keys.add(btn1, btn2)
#     keys.add(btn3, btn4)
#     return keys


def buttons_start():
    btn1 = KeyboardButton('Привет! 👋')
    btn2 = KeyboardButton('Сделать запись ✍')
    btn3 = KeyboardButton('Аналитика 🧮')
    btn4 = KeyboardButton('Информация ❓')
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

def buttons_currency_redaction():
    btn1 = KeyboardButton('-------------')
    btn2 = KeyboardButton('-------------')
    btn3 = KeyboardButton('-------------')
    btn4 = KeyboardButton('Вернуться')
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.add(btn1, btn2)
    keys.add(btn3, btn4)
    return keys




def button_delete_writes_user():
    btn_1 = InlineKeyboardButton('Удалить записи', callback_data='delete_writes')
    btn_2 = InlineKeyboardButton('Отменить', callback_data='cancel')
    inline_kb1 = InlineKeyboardMarkup()
    inline_kb1.add(btn_1)
    inline_kb1.add(btn_2)
    return inline_kb1
