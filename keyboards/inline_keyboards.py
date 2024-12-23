from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import lexicon_ru, choose_category_kb

def create_choose_category_keyboard() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = []
    for item in choose_category_kb.keys():
        buttons.append(InlineKeyboardButton(text=item, callback_data=f'category_{item}'))
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()
