from aiogram import Router, F
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackGame
from aiogram.filters import Command, CommandStart, StateFilter
from states.states import FSMFillForm
from aiogram.fsm.context import FSMContext

from keyboards.default_keyboards import create_main_menu_keyboard, create_to_income_keyboard, create_cancellation_keyboard
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
        text=lexicon_ru['start_message']
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

#К доходам из меню
@router.message(StateFilter(FSMFillForm.menu), F.text == lexicon_ru['menu_keyboard_income'])
async def process_to_income_go(message: Message, state: FSMContext):
    keyboard = create_to_income_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_income)

#Вернуться в меню
@router.message(StateFilter(FSMFillForm.to_income, FSMFillForm.to_waste), F.text == lexicon_ru['menu_keyboard_back'])
async def process_back_to_menu_from_income(message: Message, state: FSMContext):
    keyboard = create_main_menu_keyboard()
    await message.answer(
        text = lexicon_ru['go_to_menu'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.menu)

#Добавить доход
@router.message(StateFilter(FSMFillForm.to_income), F.text == lexicon_ru['income_keyboard_add'])
async def process_add_income(message: Message, state: FSMContext):
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['income_add_message_amount'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.append_income)

#отмена
@router.message(StateFilter(FSMFillForm.append_income), F.text == lexicon_ru['cancellation'])
async def process_return_to_income(message: Message, state: FSMContext):
    keyboard = create_to_income_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_income)