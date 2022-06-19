from aiogram import executor
from aiogram.utils.exceptions import BotBlocked   # для ошибок телеги
from  aiogram.utils import exceptions
from aiogram.dispatcher.filters import Command
from for_states import Currency, Analitics

import messages
from loader import dp

dp.register_message_handler(messages.start, Command('start'))
dp.register_message_handler(messages.delete_user, Command('delete_me'))

dp.register_message_handler(messages.show_button_delete_writes, Command('delete'))
dp.register_callback_query_handler(messages.delete_writes, lambda c: c.data == 'delete_writes')
dp.register_callback_query_handler(messages.cancel_delete, lambda c: c.data == 'cancel')

dp.register_message_handler(messages.hello, regexp='Привет! 👋')
dp.register_message_handler(messages.do_write, regexp='Сделать запись ✍')
dp.register_message_handler(messages.analysis, regexp='Аналитика 🧮')
dp.register_message_handler(messages.help, regexp='Информация ❓')

# currency
dp.register_message_handler(messages.main_menu, regexp='Вернуться')
dp.register_message_handler(messages.write_BYN, regexp='USD')
dp.register_message_handler(messages.write_BYN, regexp='EUR')
dp.register_message_handler(messages.write_BYN, regexp='RUB')

dp.register_message_handler(messages.write_two_curr, state=Currency.state_1)
dp.register_message_handler(messages.answer_curr, state=Currency.state_2)

dp.register_message_handler(messages.common_information, regexp='Общая информация')
dp.register_message_handler(messages.list_writes, regexp='Список записей')
dp.register_message_handler(messages.get_curr, regexp='Курсы валют')

# Тесты всякие
dp.register_message_handler(messages.geophone, regexp='/test1')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print("Бот запущен"))
