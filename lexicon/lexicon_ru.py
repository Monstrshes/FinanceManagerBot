lexicon_ru: dict[str, str] = {
    "start_message": "Привет! Я твой финансовый помощник.\n\n Нажми /help чтобы узнать, как взаимодействовать со мной.",
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
    "income_view_message_sum": "Сумма доходов за выбранный период: {}", # {} - сумма
    "income_view_message_no_income": "За этот период нет доходов.",
    "income_delete_message_confirmation": "Вы уверены, что хотите удалить выбранный доход?",
    "income_delete_message_success": "Доход успешно удален.",

    "expense_keyboard_add": "Добавить расход",
    "expense_keyboard_view": "Посмотреть расходы",
    "expense_add_message_category": "Выберите категорию расхода",
    "expense_add_message_amount": "Введите сумму расхода (число < 0):",
    "expense_add_message_description": "Введите описание расхода:",
    "expense_view_message_sum": "Сумма расходов за выбранный период: {}", # {} - сумма
    "expense_view_message_no_expense": "За этот период нет расходов.",
    "expense_delete_message_confirmation": "Вы уверены, что хотите удалить выбранный расход?",
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
    "process_to_income_go": "Вы во вкладке доходов. \n Выберите, что Вы хотите сделать дальше",
    'go_to_menu': "Снова здесь? Отлично!\nПомнишь, как легко управлять финансами с моей помощью?\nВыбирай нужный раздел из меню ниже и начинай планировать свой бюджет.",
    'cancellation': 'Отмена',
    'process_to_waste_go': 'Вы во кладке расходов.\nВыберите, что вы хотите сделать дальше'
}

LEXICON_COMMANDS = {
    '/help': 'Информация о функционале',
    '/menu': 'Вернуться в меню'
}

choose_category_kb  = {
    'Продукты': 'Это ваши тарты в категории Продукты',
    'Одежда': 'Это ваши тарты в категории Одежда',
    'Транспорт': 'Это ваши тарты в категории Транспорт',
    'Развлечения': 'Это ваши тарты в категории Развлечения',
    'Необходимое': 'Это ваши тарты в категории Необходимое',
    'Семья': 'Это ваши тарты в категории Семья',
    'Другое': 'Это ваши тарты в категории Другое'
}
