import telebot
from telebot import types
import json

from users_Classes import User
import for_request
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == "private":
        id = message.chat.id

        user = User(message.from_user)
        if user.check_unique(user):
            user.write_to_json(user)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("Курсы валют")
    markup.add(btn1, btn2, btn3)
    bot.send_message(id, text="Этот бот создается для удобства расчета покупок валюты, он может записывать и "
                              "анализировать записи покупок валюты и сравнивает ее с свежим курсом по НБРБ",
                     reply_markup=markup)

    # content_types=['photo', 'text', "sticker", "pinned_message", "audio"]
    # func=lambda message: True


def echo_all(message):
    bot.send_message(message.chat.id, message.chat.first_name + " зачем мне эта фотка?")
    print(message.chat)


@bot.message_handler(content_types=['text'])
def func(message):
    id = message.from_user.id
    if (message.text == "👋 Поздороваться"):
        bot.send_message(id, "И тебе привет")
    elif message.text == "Курсы валют":
        bot.send_message(id, "Курс доллара на сегодня: " + str(for_request.get_rate())
                         + "\nКурс евро на сегодня: " + str(for_request.get_rate(451)))
    elif message.text == "❓ Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(id, text="Задай мне вопрос", reply_markup=markup)
    elif (message.text == "Как меня зовут?"):

        bot.send_message(id, "У меня нет имени..")
    elif message.text == "Что я могу?":
        bot.send_message(id, text="сказать тебе что Деня-писюн")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Задать вопрос")
        btn3 = types.KeyboardButton("Курсы валют")
        markup.add(btn1, btn2, btn3)
        bot.send_message(id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)
