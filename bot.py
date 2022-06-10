import telebot
from telebot import types
from models.Class_User import User
import for_request
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == "private":
        current_user = User(message.from_user)
        if not User.check_unique(current_user):
            User.write_to_json(current_user)
            User.write_to_DB(current_user)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("💲 Курсы валют")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Этот бот создается для удобства расчета покупок валюты, он может записывать и "
                          "анализировать записи покупок валюты",
                     reply_markup=markup)


def echo_all(message):
    bot.send_message(message.chat.id, message.chat.first_name + " зачем мне эта фотка?")
    print(message.chat)


@bot.message_handler(content_types=['text'])
def func(message):
    id_user = message.from_user.id
    if message.text == "👋 Поздороваться":
        bot.send_message(id_user, "И тебе привет")
    elif message.text == "Курсы валют":
        bot.send_message(id_user, "Курс доллара на сегодня: " + str(for_request.get_rate())
                         + "\nКурс евро на сегодня: " + str(for_request.get_rate(451)))
    elif message.text == "❓ Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(id_user, text="Задай мне вопрос", reply_markup=markup)
    elif message.text == "Как меня зовут?":

        bot.send_message(id_user, "У меня нет имени..")
    elif message.text == "Что я могу?":
        bot.send_message(id_user, text="сказать тебе что Деня-писюн")

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Задать вопрос")
        btn3 = types.KeyboardButton("❓ Курсы валют")
        markup.add(btn1, btn2, btn2)
        markup.add(btn2, btn2, btn2)
        markup.add(btn3, btn2, btn2)
        bot.send_message(id_user, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(id_user, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
