from aiogram import Router, F
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from states.states import FSMFillForm
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from copy import deepcopy


from keyboards.default_keyboards import (create_main_menu_keyboard, create_to_income_keyboard, create_cancellation_keyboard, create_to_waste_keyboard, create_only_to_menu_kb,
                                          create_over_kb, create_yes_no_kb, create_in_piggi_bank_kb)
from keyboards.inline_keyboards import create_choose_category_keyboard, create_show_incomes_kb
from lexicon.lexicon_ru import lexicon_ru
from database.dop_bd import IN_DB, entry_data, Piggi_bank, pb, user_balances
from database.database import load_db, add_entry, show_incomes, show_wastes
from services.services import get_now_month, summ_incomes_or_wastes, create_sl_from_incomes_db


router = Router()



#/start в меню или default_state
@router.message(StateFilter(default_state), CommandStart())
async def process_start_command(message:Message, state: FSMContext):
    """
    Обрабатываем ввод команды /start в состоянии default_state или menu.
    Выводим сообщение на которое можно ответить только /help.
    """
    await message.answer(
        text=lexicon_ru['start_message']
    )
    if message.from_user.id not in IN_DB:
        load_db(message.from_user.id)
        IN_DB.append(message.from_user.id)
    user_balances[f'Balance_{message.from_user.id}'] = 0
    pb[f'Piggi_bank_{message.from_user.id}'] = deepcopy(Piggi_bank)



#/start не в default_state
@router.message(~StateFilter(default_state), CommandStart())
async def process_start_not_in_defoult(message: Message, state: FSMContext):
    """
    Обрабатываем /start в любых других состояниях.
    Выводим сообщение на которое можно ответить только /help и удаляем лишние клавиатуры и промежуточные словари.
    """
    await message.answer(
        text=lexicon_ru['start_message'],
        reply_markup=ReplyKeyboardRemove()

    )
    entry_data.clear()

#/help
@router.message(Command(commands='help'))
async def process_help_message(message: Message, state: FSMContext):
    """
    Обрабатываем команду /help в любом состоянии, что является выходом в меню.
    Выводим клавиатуру меню и удаляем промежуточные словари.
    """
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
    """
    Обрабатываем кнопку К доходам из меню.
    Переходим в сотояние to_income и выводим соответствующую клавиатуру.
    """
    keyboard = create_to_income_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_income)

#Кнопка Вернуться в меню
@router.message(StateFilter(FSMFillForm.to_income, FSMFillForm.to_waste, FSMFillForm.input_waste_ds, FSMFillForm.show_balance, FSMFillForm.other), F.text == lexicon_ru['menu_keyboard_back'])
async def process_back_to_menu_from_income(message: Message, state: FSMContext):
    """
    Обрабатывает переход пользователя в главное меню из различных состояний.

    Этот хендлер срабатывает, когда пользователь отправляет сообщение с текстом
    "menu_keyboard_back" (с кнопка "Вернуться в меню"),
    находясь в одном из следующих состояний:
        - FSMFillForm.to_income
        - FSMFillForm.to_waste
        - FSMFillForm.input_waste_ds
        - FSMFillForm.show_balance
    Хендлер создает клавиатуру главного меню и отправляет ее пользователю.
    Затем он устанавливает состояние пользователя в FSMFillForm.menu.
    """
    keyboard = create_main_menu_keyboard()
    await message.answer(
            text = lexicon_ru['go_to_menu'],
            reply_markup=keyboard
        )
    await state.set_state(FSMFillForm.menu)

#Кнопка Добавить доход
@router.message(StateFilter(FSMFillForm.to_income), F.text == lexicon_ru['income_keyboard_add'])
async def process_add_income(message: Message, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "Добавить доход".

    Этот хендлер срабатывает, когда пользователь, находясь в состоянии
    FSMFillForm.to_income, отправляет сообщение с текстом,
    соответствующим значению из словаря lexicon_ru под ключом
    'income_keyboard_add'.  В ответ на это хендлер выводит пользователю сообщение
    с просьбой ввести сумму дохода и устанавливает состояние пользователя
    в FSMFillForm.input_income, ожидая ввода суммы.
    """

    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['income_add_message_amount'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.input_income)

#Отмена из состояния input_income, input_income_ds
@router.message(StateFilter(FSMFillForm.input_income, FSMFillForm.input_income_ds), F.text == lexicon_ru['cancellation'])
async def process_return_to_income(message: Message, state: FSMContext):
    """
    Обрабатывает отмену ввода дохода, возвращая пользователя в состояние FSMFillForm.to_income.
    """
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
    """
    Переводит пользователя в раздел расходов из главного меню.
    """
    keyboard = create_to_waste_keyboard()
    await message.answer(
        text=lexicon_ru['process_to_waste_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_waste)

#Кнопка добавить расход
@router.message(StateFilter(FSMFillForm.to_waste), F.text == lexicon_ru['expense_keyboard_add'])
async def process_to_choose_category_go(message: Message, state: FSMContext):
    """
    Переводит пользователя в состояние для выбора категории расхода и выдвигает соответствующую клавиатуру
    """
    keyboard = create_choose_category_keyboard()
    await message.answer(
        text=lexicon_ru['delete_kb_mes'],
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
    """
    Возвращает пользователя к вкладке К расходам
    """
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
    """
    Обрабатывает ввод суммы дохода и помещает в словарь первичные значения
    """
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['income_add_message_description'],
        reply_markup=keyboard
    )
    entry_data['summ'] = message.text
    entry_data['type'] = 'Доход'
    entry_data['category'] = '-'
    await state.set_state(FSMFillForm.input_income_ds)

#Ввод описания дохода
@router.message(StateFilter(FSMFillForm.input_income_ds))
async def process_input_income_ds(message: Message, state: FSMContext):
    """
    Обрабатывает ввод описания дохода, заполянет словарь значениями, отправляет его в базу данных,
    изменяет текущий баланс и очищает промежуточный словраь
    """
    entry_data['description'] = message.text
    add_entry(message.from_user.id, entry_data)
    user_balances[f'Balance_{message.from_user.id}'] += int(entry_data['summ'])
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
    """
    Обрабатывает выбор категории расхода и предлагает ввести сумму расхода, а также начинает заполнять промежуточный словарь
    """
    await callback.message.answer(
        text=lexicon_ru['expense_add_message_amount']
    )
    entry_data['category'] = callback.data
    await state.set_state(FSMFillForm.input_waste)

#Ввод суммы расхода
@router.message(StateFilter(FSMFillForm.input_waste),
                lambda x: x.text.isdigit() and 0 < int(x.text))
async def process_input_waste_summ(message: Message, state: FSMContext):
    """
    Обрабатывает ввод суммы расхода, добавляет данные в промежуточный словарь
    """
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
    """
    Обрабатывает ввод описнаия расхода, заполняет до корнца промежутосный словарь,
    отправляет данные в базу данных, изменяет баланс, отслеживает, чтобы баланс был >= 0
    """
    keyboard = create_only_to_menu_kb()
    entry_data['description'] = message.text
    #Мы добавляем расход только если баланс остаётся положительным
    if user_balances[f'Balance_{message.from_user.id}'] - int(entry_data['summ']) >= 0:
        user_balances[f'Balance_{message.from_user.id}'] -= int(entry_data['summ'])
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
    """
    обрабатывает просмотр баланса. Выводит баланс.
    """
    keyboard = create_only_to_menu_kb()
    await message.answer(
        text=lexicon_ru['show_balance'].format(user_balances[f'Balance_{message.from_user.id}']),
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.show_balance)

#Кнопка Посмотреть доходы
@router.message(StateFilter(FSMFillForm.to_income), F.text == lexicon_ru['income_keyboard_view'])
async def process_view_incomes(message: Message, state: FSMContext):
    """
    Обрабатывает просмотр доходов.

    Получает текущий месяц, загружает доходы пользователя, создает клавиатуру,
    выводит сумму доходов и переводит пользователя в следующее состояние.
    """
    current_month = get_now_month()
    lst = show_incomes(message.from_user.id, current_month)
    keyboard = create_show_incomes_kb(lst)
    sl_for_inline = create_sl_from_incomes_db(lst)
    summ = summ_incomes_or_wastes(lst)
    await message.answer(
        text=lexicon_ru['delete_kb_mes'],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=  lexicon_ru['income_view_message_sum'].format(summ),
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.show_income)
    await state.update_data(sl_for_inline=sl_for_inline) # Мы сохраняем переменную `sl_for_inline` в контексте пользователя под ключом `sl_for_inline`.

#Обработка нажатий на инлан кнопки
@router.callback_query(StateFilter(FSMFillForm.show_income), F.data != 'cancelation')
async def process_give_description_income(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатываем нажатия на инлайн-кнопки
    """
    keyboard = create_cancellation_keyboard()
    data = await state.get_data() # получаем все сохраненные данные
    sl_for_inline = data.get("sl_for_inline") # получаем sl_for_inline
    await callback.message.answer(
        text=lexicon_ru['income_show_description'].format(sl_for_inline[f'{callback.data}'][0],sl_for_inline[f'{callback.data}'][1] ),
        reply_markup=keyboard
    )

#Обработка нажатия инлайн-кнопки Отмена в соответствующем состоянии
@router.callback_query(StateFilter(FSMFillForm.show_income), F.data == 'cancelation')
async def process_cancellation_in_show_income(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатываем нажатие инлайн кнопки Отмена среди Расходов
    """
    keyboard = create_to_income_keyboard()
    await callback.message.answer(
        text=lexicon_ru['process_to_income_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_income)

#Кнопка отмена из конкертного дохода
@router.message(StateFilter(FSMFillForm.show_income), F.text == 'Отмена')
async def process_cancellation_from_concr_income(message: Message, state: FSMContext):
    """
    Обрабатываем нажитие кнопки Отмена из просмотра конкретного дохода и возвращаем пользователя обратно ко всем доходам
    """
    current_month = get_now_month()
    lst = show_incomes(message.from_user.id, current_month)
    keyboard = create_show_incomes_kb(lst)
    sl_for_inline = create_sl_from_incomes_db(lst)
    summ = summ_incomes_or_wastes(lst)
    await message.answer(
        text=lexicon_ru['delete_kb_mes'],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=  lexicon_ru['income_view_message_sum'].format(summ),
        reply_markup=keyboard
    )
    await state.update_data(sl_for_inline=sl_for_inline) # Мы сохраняем переменную `sl_for_inline` в контексте пользователя под ключом `sl_for_inline`.

#Кнопка Посмотреть расходы
@router.message(StateFilter(FSMFillForm.to_waste), F.text == lexicon_ru['expense_keyboard_view'])
async def process_to_choose_category_to_show_wastes(message: Message, state: FSMContext):
    keyboard = create_choose_category_keyboard()
    await message.answer(
        text=lexicon_ru['delete_kb_mes'],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=lexicon_ru['expense_add_message_category_to_show'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.show_waste)

#одна из инлайн кнопок с категориями
@router.callback_query(StateFilter(FSMFillForm.show_waste), F.data.in_(['Продукты', 'Одежда', 'Транспорт', 'Развлечения', 'Необходимое', 'Семья', 'Другое']))
async def process_view_wastes(callback: CallbackQuery, state: FSMContext):
    current_month = get_now_month()
    lst = show_wastes(callback.message.chat.id, current_month, callback.data)
    keyboard = create_show_incomes_kb(lst)
    sl_for_inline = create_sl_from_incomes_db(lst)
    summ = summ_incomes_or_wastes(lst)
    await callback.message.answer(
        text=lexicon_ru['delete_kb_mes'],
        reply_markup=ReplyKeyboardRemove()
    )
    await callback.message.answer(
        text=  lexicon_ru['expense_view_message_sum'].format(callback.data, summ, callback.data),
        reply_markup=keyboard
    )
    await state.update_data(sl_for_inline=sl_for_inline) # Мы сохраняем переменную `sl_for_inline` в контексте пользователя под ключом `sl_for_inline`.
    await state.update_data(category_now=callback.data)

#Обработка нажатий на инлан кнопки
@router.callback_query(StateFilter(FSMFillForm.show_waste), F.data != 'cancelation')
async def process_give_description_income(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатываем нажатия на инлайн-кнопки
    """
    keyboard = create_cancellation_keyboard()
    data = await state.get_data() # получаем все сохраненные данные
    sl_for_inline = data.get("sl_for_inline") # получаем sl_for_inline
    await callback.message.answer(
        text=lexicon_ru['waste_show_description'].format(sl_for_inline[f'{callback.data}'][0],sl_for_inline[f'{callback.data}'][1] ),
        reply_markup=keyboard
    )

#Обработка нажатия инлайн-кнопки Отмена в соответствующем состоянии
@router.callback_query(StateFilter(FSMFillForm.show_waste), F.data == 'cancelation')
async def process_cancellation_in_show_income(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатываем нажатие инлайн кнопки Отмена среди Расходов
    """
    keyboard = create_to_waste_keyboard()
    await callback.message.answer(
        text=lexicon_ru['process_to_waste_go'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.to_waste)

#Кнопка отмена из конкертного дохода
@router.message(StateFilter(FSMFillForm.show_waste), F.text == 'Отмена')
async def process_cancellation_from_concr_income(message: Message, state: FSMContext):
    """
    Обрабатываем нажитие кнопки Отмена из просмотра конкретного дохода и возвращаем пользователя обратно ко всем доходам
    """
    data = await state.get_data() # получаем все сохраненные данные
    category = data.get("category_now")
    current_month = get_now_month()
    lst = show_wastes(message.from_user.id, current_month, category)
    keyboard = create_show_incomes_kb(lst)
    sl_for_inline = create_sl_from_incomes_db(lst)
    summ = summ_incomes_or_wastes(lst)
    await message.answer(
        text=lexicon_ru['delete_kb_mes'],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text= lexicon_ru['expense_view_message_sum'].format(category, summ, category),
        reply_markup=keyboard
    )
    await state.update_data(sl_for_inline=sl_for_inline) # Мы сохраняем переменную `sl_for_inline` в контексте пользователя под ключом `sl_for_inline`.


#Кнопка другое из меню
@router.message(StateFilter(FSMFillForm.menu), F.text == lexicon_ru['menu_keyboard_other'])
async def process_to_other_go(message: Message, state: FSMContext):
    """
    Обрабатываем нажатие кнопки Другое из меню и выводим соответствующую клавиатуру
    """
    keyboard = create_over_kb()
    await message.answer(
        text = lexicon_ru['in_other_menu_message'],
        reply_markup=keyboard
    )

    await state.set_state(FSMFillForm.other)

@router.message(StateFilter(FSMFillForm.other), F.text == lexicon_ru['to_piggy_bank_go'])
async def process_to_piggi_bank_go(message: Message, state: FSMContext):
    """
    Обрабатываем переход в копилку
    """
    if pb[f'Piggi_bank_{message.from_user.id}']['is_goal'] == False:
        keyboard = create_yes_no_kb()
        await message.answer(
            text=lexicon_ru['first_time_in_piggi_bank'],
            reply_markup=keyboard
        )
        await state.set_state(FSMFillForm.create_pb)
    else:
        keyboard1 = create_in_piggi_bank_kb()
        await message.answer(
            text = lexicon_ru['piggi_bank_text'].format(pb[f'Piggi_bank_{message.from_user.id}']['goal_summ'], pb[f'Piggi_bank_{message.from_user.id}']['goal_descr'], pb[f'Piggi_bank_{message.from_user.id}']['summa']),
            reply_markup=keyboard1
        )
        await state.set_state(FSMFillForm.to_piggi_bank)

@router.message(StateFilter(FSMFillForm.create_pb), F.text == 'Да')
async def process_create_piggi_bank(message: Message, state: FSMContext):
    """
    Обрабатываем согласие на создание копилки и переводим пользователя к её заполнению
    """
    await message.answer(
        text=lexicon_ru['create_piggi_bank_summ'],
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(FSMFillForm.create_pb_summ)

@router.message(StateFilter(FSMFillForm.create_pb_summ), lambda x: x.text.isdigit() and 0 < int(x.text))
async def process_create_piggi_bank_summ(message: Message, state: FSMContext):
    """
    Обрабатываем ввод суммы накопления и переводим пользователя к описанию цели
    """
    await message.answer(
        text=lexicon_ru['create_piggi_bank_descr']
    )
    pb[f'Piggi_bank_{message.from_user.id}']['goal_summ'] = int(message.text)
    await state.set_state(FSMFillForm.create_pb_descr)

@router.message(StateFilter(FSMFillForm.create_pb_descr))
async def process_create_piggi_bank_descr(message: Message, state: FSMFillForm):
    """
    Обрабатываем ввод описания цели накопления и преводим в главное меню копилки
    """
    pb[f'Piggi_bank_{message.from_user.id}']['goal_descr'] = message.text
    pb[f'Piggi_bank_{message.from_user.id}']['is_goal'] = True
    keyboard1 = create_in_piggi_bank_kb()
    await message.answer(
        text = lexicon_ru['piggi_bank_text'].format(pb[f'Piggi_bank_{message.from_user.id}']['goal_summ'], pb[f'Piggi_bank_{message.from_user.id}']['goal_descr'], pb[f'Piggi_bank_{message.from_user.id}']['summa']),
        reply_markup=keyboard1
    )
    await state.set_state(FSMFillForm.to_piggi_bank)

@router.message(StateFilter(FSMFillForm.to_piggi_bank), F.text == lexicon_ru['piggi_bank_add_money'])
async def process_save_up_more_to_pb(message: Message, state: FSMContext):
    """
    Обрабатываем кнопку Отложить ещё и просим ввести сумму, которая спишется с баланса
    """
    keyboard = create_cancellation_keyboard()
    await message.answer(
        text=lexicon_ru['save_up_to_piggi_bank'],
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.save_up_more_pb)

@router.message(StateFilter(FSMFillForm.save_up_more_pb), lambda x: x.text.isdigit() and 0 < int(x.text))
async def process_input_summ_to_save_up(message: Message, state: FSMContext):
    """
    Обрабатываем ввод суммы, увеличение суммы в копилке и уменьшение баланса
    """

    if user_balances[f'Balance_{message.from_user.id}'] - int(message.text) >= 0:
        user_balances[f'Balance_{message.from_user.id}'] -= int(message.text)
        pb[f'Piggi_bank_{message.from_user.id}']['summa'] += int(message.text)
        keyboard1 = create_in_piggi_bank_kb()
        await message.answer(
            text='Успешно!'
        )
        await message.answer(
        text = lexicon_ru['piggi_bank_text'].format(pb[f'Piggi_bank_{message.from_user.id}']['goal_summ'], pb[f'Piggi_bank_{message.from_user.id}']['goal_descr'], pb[f'Piggi_bank_{message.from_user.id}']['summa']),
        reply_markup=keyboard1
    )
        await state.set_state(FSMFillForm.to_piggi_bank)
    else:
       keyboard = create_cancellation_keyboard()
       await message.answer(
           text = lexicon_ru['save_up_to_piggi_bank_eror'],
           reply_markup=keyboard
       )

@router.message(StateFilter(FSMFillForm.save_up_more_pb), F.text == lexicon_ru['cancellation'])
async def process_cancellation_from_piggi_bank(message: Message, state: FSMContext):
    """
    Обрабатываем сразу две кнопки ОТМЕНА и возвращаем в меню копилки
    """
    keyboard1 = create_in_piggi_bank_kb()
    await message.answer(
        text = lexicon_ru['piggi_bank_text'].format(pb[f'Piggi_bank_{message.from_user.id}']['goal_summ'], pb[f'Piggi_bank_{message.from_user.id}']['goal_descr'], pb[f'Piggi_bank_{message.from_user.id}']['summa']),
        reply_markup=keyboard1
    )
    await state.set_state(FSMFillForm.to_piggi_bank)

@router.message(StateFilter(FSMFillForm.to_piggi_bank), F.text == lexicon_ru['back'])
async def process_back_to_other_from_pb(message: Message, state: FSMContext):
    keyboard = create_over_kb()
    await message.answer(
        text = lexicon_ru['in_other_menu_message'],
        reply_markup=keyboard
    )

    await state.set_state(FSMFillForm.other)

@router.message(StateFilter(FSMFillForm.to_piggi_bank), F.text == lexicon_ru['piggi_bank_change_goal'])
async def process_change_goal_in_pb(message: Message, state: FSMContext):
    await message.answer(
        text=lexicon_ru['create_piggi_bank_summ'],
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(FSMFillForm.create_pb_summ)