from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup,ReplyKeyboardRemove
from lexicon.lexicon_ru import lexicon_ru

def create_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Создает основную клавиатуру с кнопками."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=lexicon_ru["menu_keyboard_income"]),
                KeyboardButton(text=lexicon_ru["menu_keyboard_waste"]),
            ],
            [
               KeyboardButton(text=lexicon_ru["menu_keyboard_balance"])
            ],
            [KeyboardButton(text=lexicon_ru["menu_keyboard_other"])]

        ],
        resize_keyboard=True,
    )
    return keyboard

def create_to_income_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=lexicon_ru['income_keyboard_add'])],
        [KeyboardButton(text=lexicon_ru['income_keyboard_view'])],
        [KeyboardButton(text=lexicon_ru['menu_keyboard_back'])]
        ],
        resize_keyboard=True
    )
    return keyboard

def create_cancellation_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=lexicon_ru['cancellation'])]],
        resize_keyboard=True
    )
    return keyboard