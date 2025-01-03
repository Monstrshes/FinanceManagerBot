lexicon_ru: dict[str, str] = {
    "start_message": "<b>Привет!</b> Я твой финансовый помощник.\n\nНажми /help чтобы узнать, как взаимодействовать со мной.",
    "help_message": "Я помогаю тебе контролировать доходы и расходы.\n\nИспользуй меню для добавления, просмотра и управления своими финансами.\n\n*Основные команды:*\n/start - начать работу\n/help - помощь.\nВоспользуйтесь ими или кнопками снизу.",
    "menu_keyboard_income": "К доходам",
    "menu_keyboard_waste": "К расходам",
    "menu_keyboard_balance": "Баланс",
    "menu_keyboard_other": "Другое",
    "menu_keyboard_back": "Вернуться в меню",


    "income_keyboard_add": "Добавить доход",
    "income_keyboard_view": "Посмотреть доходы",
    "income_add_message_amount": "Введите сумму дохода (число > 0):",
    "income_add_message_description": "Введите описание дохода:",
    "income_view_message_sum": "Сумма доходов за этот месяц = <b>{}</b>.\n\nНиже вы видите все ваши доходы. Нажмите на соответствующую кнопку, чтобы увидеть время добавления дохода и его описание. ", # {} - сумма
    "income_view_message_no_income": "За этот период нет доходов.",
    "income_delete_message_confirmation": "Вы уверены, что хотите удалить выбранный доход?",
    "income_delete_message_success": "Доход успешно удален.",
    "income_show_description": "Этот доход был добавлен {}. \n\nОписание: \n{}", #{} - дата, описание

    "expense_keyboard_add": "Добавить расход",
    "expense_keyboard_view": "Посмотреть расходы",
    "expense_add_message_category": "Выберите категорию расхода",
    "expense_add_message_amount": "Введите сумму расхода (число > 0):",
    "expense_add_message_description": "Введите описание расхода:",
    "expense_view_message_sum": "Сумма расходов за этот месяц в категории {} = <b>{}</b>.\n\nНиже вы видите все ваши расходы в категории {}. Нажмите на соответствующую кнопку, чтобы увидеть время добавления расхода и его описание. ", # {} - сумма
    "expense_view_message_no_expense": "За этот период нет расходов.",
    "expense_delete_message_confirmation": "Вы уверены, что хотите удалить выбранный расход?",
    "waste_show_description": "Этот доход был добавлен {}. \n\nОписание: \n{}", #{} - дата, описаниб
    "expense_delete_message_success": "Расход успешно удален.",

    "balance_message_balance": "Ваш текущий баланс: {}.\nСамый большой расход: {}.", # {} - баланс, {} - самый большой расход
    "balance_message_no_transactions": "У вас пока нет транзакций.",

    "other_keyboard_limit": "Добавить лимит",
    "other_keyboard_report": "Вывести отчёт",

    "limit_add_message_category": "Выберите категорию для установки лимита:",
    "limit_add_message_amount": "Введите сумму лимита (число > 0):",
    "limit_add_message_set_success": "Лимит установлен на {category}: {}" ,  # {} - категория, {} - лимит
    "report_select_period": "Выберите период для отчёта:",
    "report_period_month": "Месяц",
    "report_period_year": "Год",
    "report_period_all": "За всё время",
    "report_select_format": "Выберите формат отчета",
    "report_format_text": "Текст",
    "report_format_graphics": "График",
    "report_no_data": "Нет данных для отчёта за выбранный период.",
   "report_message_text": "Отчёт за выбранный период",
    "report_message_graphics": "График за выбранный период",

    "button_cancel": "Отмена",
    "error_invalid_input_amount": "Неверный формат суммы. Введите число.",
    "error_invalid_input_description": "Неверный формат описания.",
    "error_category_not_selected": "Выберите категорию.",

    "limit_keyboard_set_limit": "Установить лимит",
    "limit_keyboard_view_limits": "Посмотреть лимиты",
    "limit_message_set_limit": "Выберите категорию для установления лимита.",
    "limit_message_no_limits": "У вас пока нет лимитов.",

    "error_message" : 'Что-то пошло не так. Нажмите /help, чтобы вернуться в меню',
    "process_to_income_go": "Вы во вкладке доходов. \nВыберите, что Вы хотите сделать дальше",
    'go_to_menu': "Снова здесь? Отлично!\nПомнишь, как легко управлять финансами с моей помощью?\nВыбирай нужный раздел из меню ниже и начинай планировать свой бюджет.",
    'cancellation': 'Отмена',
    'process_to_waste_go': 'Вы во кладке расходов.\nВыберите, что вы хотите сделать дальше',
    'balance_error': '<b>Баланс не может быть меньше 0!!!</b>\nВероятно, вы не добавили какие-либо доходы',
    'show_balance': 'Ваш текущий баланс равен <b>{}</b>. Потратьте его с умом!',
    'delete_kb_mes': 'Удаляем ненужную клавиатуру)',
    'expense_add_message_category_to_show': 'Выберите категорию, в которой хотите посмотреть расходы',
    'to_piggy_bank_go': 'Перейти в копилку🐷',
    'in_other_menu_message': 'Вы во вкладке "Другое"\nЗдесь находится дополнительный, но не менее важный функционал Вашего финансового помощника!',
    'first_time_in_piggi_bank': 'Привет!\nЭто твоя <b>Копилка</b>!\nНо у тебя пока нет цели накопления(\nХочешь создать свою копилку?',
    'piggi_bank_text':'Это ваша Копилка!\nВаша цель накопить <b>{}</b> рублей, чтобы {}\n\nСейчас у вас накоплено <b>{}</b> рублей. \n\nПродолжайте в том же духе и у вас всё получится!', #сумма цели, описание цели, сумма сейчас
    'piggi_bank_add_money': 'Отложить ещё',
    'piggi_bank_change_goal': 'Изменить цель',
    'create_piggi_bank_summ': 'Введите сумму, которую хотите накопить: (>0)',
    'create_piggi_bank_descr': 'Введите цель вашего накопления, чтобы в дальнейшем она мотивировала вас откладывать!',
    'save_up_to_piggi_bank': 'Введите сумму, которую хотите отложить (>0). \nОна спишется с вашего баланса.',
    'save_up_to_piggi_bank_eror': 'У вас на балансе нет такой суммы!',
    'back': 'Назад',
    'save_up_percent_of_income':'Это достаточно большой доход!\nПредлагаю отложить часть от него в вашу Копилку!',
    'piggi_bank_text_nearly_to_goal':'Это ваша Копилка!\nВаша цель накопить <b>{}</b> рублей, чтобы {}\n\nСейчас у вас накоплено <b>{}</b> рублей. \n\nВы почти у цели! Вам осталось накоить менее 20%!',
    'piggi_bank_get_goal': 'Поздравляю!!! Вы достигли цели и накопили {} рублей!! \nТеперь вы можете {}! Ваша сумма уже на балансе, скорее потратьте её!',
    'chart_for_month_button': 'Вывести отчёт за месяц',
    'chart_for_month_message': 'Это визуализированная диаграмма ваших расходов за этот месяц'
    }

LEXICON_COMMANDS = {
    '/start': 'Перезапустить бота',
    '/help': 'Помощь или Вернуться в меню'
}

choose_category_kb  = {
    'Продукты': 'Это ваши траты в категории Продукты',
    'Одежда': 'Это ваши траты в категории Одежда',
    'Транспорт': 'Это ваши траты в категории Транспорт',
    'Развлечения': 'Это ваши траты в категории Развлечения',
    'Необходимое': 'Это ваши траты в категории Необходимое',
    'Семья': 'Это ваши траты в категории Семья',
    'Другое': 'Это ваши траты в категории Другое'
}
