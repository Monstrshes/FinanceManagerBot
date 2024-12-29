from aiogram import Router, F
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from states.states import FSMFillForm
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default_keyboards import create_main_menu_keyboard, create_to_income_keyboard, create_cancellation_keyboard, create_to_waste_keyboard, create_only_to_menu_kb
from keyboards.inline_keyboards import create_choose_category_keyboard
from lexicon.lexicon_ru import lexicon_ru
from database.dop_bd import IN_DB, entry_data
from database.database import load_db, add_entry

router = Router()
Balance = 0 #Переменная для подсчета баланса


#/start в меню или default_state
@router.message(StateFilter(default_state), CommandStart())
async def process_start_command(message:Message, state: FSMContext):
    await message.answer(
        text=lexicon_ru['start_message']
    )
    if message.from_user.id not in IN_DB:
        load_db(message.from_user.id)
        IN_DB.append(message.from_user.id)


#/start не в default_state
@router.message(~StateFilter(default_state), CommandStart())
async def process_start_not_in_defoult(message: Message, state: FSMContext):
    await message.answer(
        text=lexicon_ru['start_message'],
        reply_markup=ReplyKeyboardRemove()

    )
    entry_data.clear()

#/help
@router.message(Command(commands='help'))
async def process_help_message(message: Message, state: FSMContext):
    keyboard = create_main_menu_keyboard()
    await message.answer(
        text=lexicon_ru['help_message'],
        reply_markup=keyboard
    )
    entry_data.clear()
    await state.set_state(FSMFillForm.menu)

#кнопка К доходам из меню
@router.message(StateFilter(FSMFillForm.menu), F.text == lexicon_ru['menu_keyboard_income'])
async def process_to_income_go(message: Message, state: FSMContext):
    keyboard = create_to_income_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_income)

#Кнопка Вернуться в меню
@router.message(StateFilter(FSMFillForm.to_income, FSMFillForm.to_waste, FSMFillForm.input_waste_ds, FSMFillForm.show_balance), F.text == lexicon_ru['menu_keyboard_back'])
async def process_back_to_menu_from_income(message: Message, state: FSMContext):
    keyboard = create_main_menu_keyboard()
    await message.answer(
            text = lexicon_ru['go_to_menu'],
            reply_markup=keyboard
        )
    await state.set_state(FSMFillForm.menu)

#Кнопка Добавить доход
@router.message(StateFilter(FSMFillForm.to_income), F.text == lexicon_ru['income_keyboard_add'])
async def process_add_income(message: Message, state: FSMContext):
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['income_add_message_amount'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.input_income)

#Отмена из состояния input_income, input_income_ds
@router.message(StateFilter(FSMFillForm.input_income, FSMFillForm.input_income_ds), F.text == lexicon_ru['cancellation'])
async def process_return_to_income(message: Message, state: FSMContext):
    keyboard = create_to_income_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    entry_data.clear()
    await state.set_state(FSMFillForm.to_income)

#к расходам из меню
@router.message(StateFilter(FSMFillForm.menu), F.text == lexicon_ru['menu_keyboard_waste'])
async def process_to_waste_go(message: Message, state: FSMContext):
    keyboard = create_to_waste_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_waste_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_waste)

#Кнопка добавить расход
@router.message(StateFilter(FSMFillForm.to_waste), F.text == lexicon_ru['expense_keyboard_add'])
async def process_to_choose_category_go(message: Message, state: FSMContext):
    keyboard = create_choose_category_keyboard()
    await message.answer(
        text='Удаление старой клавиатуры)',
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=lexicon_ru['expense_add_message_category'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.choose_category)


#Отмена из состояния choose_category, input_waste, input_waste_ds
@router.message(StateFilter(FSMFillForm.choose_category, FSMFillForm.input_waste, FSMFillForm.input_waste_ds), F.text == lexicon_ru['cancellation'])
async def process_return_to_income(message: Message, state: FSMContext):
    keyboard = create_to_waste_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_waste_go'],
        reply_markup=keyboard
    )
    entry_data.clear()
    await state.set_state(FSMFillForm.to_waste)

#Ввод суммы дохода
@router.message(StateFilter(FSMFillForm.input_income),
                lambda x: x.text.isdigit() and 0 < int(x.text))
async def process_input_income_summ(message: Message, state: FSMContext):
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['expense_add_message_description'],
        reply_markup=keyboard
    )
    entry_data['summ'] = message.text
    entry_data['type'] = 'Доход'
    entry_data['category'] = '-'
    await state.set_state(FSMFillForm.input_income_ds)

#Ввод описания дохода
@router.message(StateFilter(FSMFillForm.input_income_ds))
async def process_input_income_ds(message: Message, state: FSMContext):
    global Balance
    entry_data['description'] = message.text
    add_entry(message.from_user.id, entry_data)
    Balance += int(entry_data['summ'])
    entry_data.clear()
    await state.set_state(FSMFillForm.menu)
    keyboard = create_main_menu_keyboard()
    await message.answer(
            text = lexicon_ru['go_to_menu'],
            reply_markup=keyboard
        )

#Выбор кнокпи с категорией
@router.callback_query(StateFilter(FSMFillForm.choose_category),F.data.in_(['Продукты', 'Одежда', 'Транспорт', 'Развлечения', 'Необходимое', 'Семья', 'Другое']))
async def process_input_waste(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=lexicon_ru['expense_add_message_amount']
    )
    entry_data['category'] = callback.data
    await state.set_state(FSMFillForm.input_waste)

#Ввод суммы расхода
@router.message(StateFilter(FSMFillForm.input_waste),
                lambda x: x.text.isdigit() and 0 < int(x.text))
async def process_input_waste_summ(message: Message, state: FSMContext):
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['expense_add_message_description'],
        reply_markup=keyboard
    )
    entry_data['summ'] = message.text
    entry_data['type'] = 'Расход'
    await state.set_state(FSMFillForm.input_waste_ds)

#Ввод описания расхода
@router.message(StateFilter(FSMFillForm.input_waste_ds), F.text != 'Вернуться в меню')
async def process_input_waste_ds(message: Message, state: FSMContext):
    keyboard = create_only_to_menu_kb()
    global Balance
    entry_data['description'] = message.text
    #Мы добавляем расход только если баланс остаётся положительным
    if Balance - int(entry_data['summ']) >= 0:
        Balance -= int(entry_data['summ'])
        add_entry(message.from_user.id, entry_data)
        entry_data.clear()
        await state.set_state(FSMFillForm.menu)
        keyboard1 = create_main_menu_keyboard()
        await message.answer(
            text = lexicon_ru['go_to_menu'],
            reply_markup=keyboard1
        )
    #Иначе вызываем своё исключение(не совсем)
    else:
        await message.answer(
            text=lexicon_ru['balance_error'],
            reply_markup=keyboard
        )
        entry_data.clear()

#Кнопка Баланс из меню
@router.message(StateFilter(FSMFillForm.menu), F.text == lexicon_ru['menu_keyboard_balance'])
async def process_show_balance(message: Message, state: FSMContext):
    global Balance
    keyboard = create_only_to_menu_kb()
    await message.answer(
        text=lexicon_ru['show_balance'].format(Balance),
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.show_balance)
