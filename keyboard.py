from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

analysis_two_row = [['Общая информация', 'Список записей'], ['Курсы валют', 'Вернуться']]
start_two_row = [['Привет! 👋', 'Сделать запись ✍'], ['Аналитика 🧮', 'Информация ❓']]
currency_two_row = [['USD', 'EUR'], ['RUB', 'Вернуться']]
currency_two_row_state_2 = [['---', '---'], ['---', 'Вернуться']]

myfin = [['Подробнее на myfin.by ', '', "https://myfin.by/currency/minsk"]]
delete_writes_inline = [['Удалить записи', 'delete_writes'], ['Отменить', 'cancel']]


def get_buttons_one_row(namekeys: []):
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in namekeys:
        btn = KeyboardButton(i)
        keys.add(btn)
    return keys


def get_button_more_one_row(namekeys):
    """Созданно что бы было меньше кода при создании кнопок
    аргумент функции должен быть вида ['Кнопка1', 'Кнопка2']"""
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in namekeys:
        if len(i) == 2:
            btn1 = KeyboardButton(i[0])
            btn2 = KeyboardButton(i[1])
            keys.add(btn1, btn2)
        elif len(i) > 2:
            for j in i:
                btn = KeyboardButton(j)
                keys.insert(btn)
    return keys


def get_inline_buttons(namekeys):
    """Созданно что бы было меньше кода при создании инлайн кнопок
    [0] -> text
    [1] ->callback_data
    [2] -> url
    пример 1: str = [['text_1', 'callback_data_1'], ['text_2', 'callback_data_2']] -> без url
    пример 2: str = [['text', '', 'url']] -> без callback_data"""
    inline_keys = InlineKeyboardMarkup()
    count = len(namekeys)
    for i in namekeys:
        btn = InlineKeyboardButton("null")
        if len(i) >= 0:
            btn.text = i[0]
        if len(i) >= 1 and i[1] != '':
            btn.callback_data = i[1]
        if len(i) > 2:
            btn.url = i[2]
        inline_keys.insert(btn)
    return inline_keys

