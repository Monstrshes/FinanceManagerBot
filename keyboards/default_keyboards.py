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

#кнопка отмена
def create_cancellation_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=lexicon_ru['cancellation'])]],
        resize_keyboard=True
    )
    return keyboard

def create_to_waste_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=lexicon_ru['expense_keyboard_add'])],
        [KeyboardButton(text=lexicon_ru['expense_keyboard_view'])],
        [KeyboardButton(text=lexicon_ru['menu_keyboard_back'])]
        ],
        resize_keyboard=True
    )
    return keyboard

def create_only_to_menu_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=lexicon_ru['menu_keyboard_back'])]],
        resize_keyboard=True
    )
    return keyboard

def create_over_kb() -> ReplyKeyboardMarkup:
    """
    Создаём клавиатуру во вкладке другое
    1. Перейти к копилке
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=lexicon_ru['to_piggy_bank_go'])],
                  [KeyboardButton(text=lexicon_ru['menu_keyboard_back'])]
                  ],
        resize_keyboard=True
    )
    return keyboard

def create_yes_no_kb() -> ReplyKeyboardMarkup:
    """
    Создаем клавиатуру Да/нет
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Да'), KeyboardButton(text='Нет')],

        ],
        resize_keyboard=True
    )
    return keyboard

def create_in_piggi_bank_kb() -> ReplyKeyboardMarkup:
    """
    Создаём клавиатуру раздела Копилка
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=lexicon_ru['piggi_bank_add_money'])],
            [KeyboardButton(text=lexicon_ru['piggi_bank_change_goal'])],
            [KeyboardButton(text=lexicon_ru['back'])]
        ],
        resize_keyboard=True
    )
    return keyboard

def create_save_up_percent_of_income_kb() -> ReplyKeyboardMarkup:
    """
    создаём клавиатуру, которая предложит пользователю отложить часть дохода в копилку
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Отложить 5%')],
            [KeyboardButton(text='Отложить 10%')],
            [KeyboardButton(text='Ничего не откладывать')]
        ],
        resize_keyboard=True
    )
    return keyboard

def create_only_go_to_menu_kb() -> ReplyKeyboardMarkup:
    """
    Создаём клавиатуру с кнопкой вернуться в меню
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=lexicon_ru['menu_keyboard_back'])]
        ],
        resize_keyboard=True
    )
    return keyboard
