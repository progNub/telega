import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     """Этот бот создается для удобства
                     расчета покупок валюты, он может
                     записывать и анализировать записи
                     покупок валюты и сравнивает ее с свежим курсом""")


# content_types=['photo', 'text', "sticker", "pinned_message", "audio"]
# func=lambda message: True

@bot.message_handler(content_types=['photo', 'text', "sticker", "pinned_message", "audio"])
def echo_all(message):
    bot.send_message(message.chat.id, message.chat.username + " ты кожанный ублюдок")


bot.polling()
