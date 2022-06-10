from aiogram.utils.helper import Helper, HelperMode
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class Currency(StatesGroup):
    state_1 = State()
    state_2 = State()
    state_run = State()
