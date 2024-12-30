from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import lexicon_ru, choose_category_kb

#Создает клавиатуру с категориями
def create_choose_category_keyboard() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = []
    for item in choose_category_kb.keys():
        buttons.append(InlineKeyboardButton(text=item, callback_data=item))
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

#создаёт клавиатуру с доходами в порядке возрастания+отмена
def create_show_incomes_kb(lst: list) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = []
    for item in lst:
        buttons.append(InlineKeyboardButton(text=str(item[0]), callback_data=f'{item[0]}_{item[2]}'))
    button_cancel = InlineKeyboardButton(text='Отмена', callback_data='cancelation')
    buttons.append(button_cancel)
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()