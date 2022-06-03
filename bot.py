import telebot
import json
import for_request
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Этот бот создается для удобства расчета покупок валюты, он может записывать и "
                     "анализировать записи покупок валюты и сравнивает ее с свежим курсом" + "\n\nКурс доллара на сегодня: "
                     + str(for_request.DOLLAR.get('Cur_OfficialRate')))


# content_types=['photo', 'text', "sticker", "pinned_message", "audio"]
# func=lambda message: True

@bot.message_handler(content_types=['photo'])
def echo_all(message):
    bot.send_message(message.chat.id, message.chat.first_name + " зачем мне эта фотка?")
    print(message.chat)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, message.chat.first_name + " привет")
    print(message.text)


bot.polling()
