from aiogram import Router, F
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackGame
from aiogram.filters import Command, CommandStart, StateFilter
from states.states import FSMFillForm
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default_keyboards import create_main_menu_keyboard, create_to_income_keyboard, create_cancellation_keyboard, create_to_waste_keyboard
from keyboards.inline_keyboards import create_choose_category_keyboard
from lexicon.lexicon_ru import lexicon_ru

router = Router()


#/start в меню или default_state
@router.message(StateFilter(default_state), CommandStart())
async def process_start_command(message:Message, state: FSMContext):
    await message.answer(
        text=lexicon_ru['start_message']
    )

#/start не в default_state
@router.message(~StateFilter(default_state), CommandStart())
async def process_start_not_in_defoult(message: Message, state: FSMContext):
    await message.answer(
        text=lexicon_ru['start_message'],
        reply_markup=ReplyKeyboardRemove()

    )

#/help
@router.message(Command(commands='help'))
async def process_help_message(message: Message, state: FSMContext):
    keyboard = create_main_menu_keyboard()
    await message.answer(
        text=lexicon_ru['help_message'],
        reply_markup=keyboard
    )
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
@router.message(StateFilter(FSMFillForm.to_income, FSMFillForm.to_waste), F.text == lexicon_ru['menu_keyboard_back'])
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
    keyboard1 = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['expense_add_message_category'],
        reply_markup=keyboard
    )
    await message.answer(
        text = ':',
        reply_markup=keyboard1
    )
    await state.set_state(FSMFillForm.choose_category)


#Отмена из состояния choose_category, input_waste, input_waste_ds
@router.message(StateFilter(FSMFillForm.choose_category, FSMFillForm.input_waste, FSMFillForm.input_waste_ds), F.text == lexicon_ru['cancellation'])
async def process_return_to_income(message: Message, state: FSMContext):
    keyboard = create_to_waste_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_waste)