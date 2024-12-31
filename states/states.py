#Файл для создания машины сосотояний


from aiogram.fsm.state import  State, StatesGroup

class FSMFillForm(StatesGroup):
    menu = State()

    to_income = State() #Состояние после нажатия из меню кнопки к доходам
    show_income  = State() #Состояние для просмотра доходов
    input_income = State() #Состояние для ввода дохода как числа
    input_income_ds = State() ##Состояние для ввода описания дохода

    to_waste = State() #Состояние после нажатия из меню кнопки к расходам
    choose_category = State() #Состояние для выбора для добавления расхода
    show_waste = State() #Состояние для просмотра расходов
    input_waste = State() #Состояние для ввода расхода как числа
    input_waste_ds = State() ##Состояние для ввода описания расхода

    show_balance = State() #состояние для простмотра баланса

    other = State() #Состояние после нажатия из менб кнопки Другое

    to_piggi_bank = State() #Состояние для работы с копилкой
    create_pb = State() #согласие или отказ создание новой копилки
    create_pb_summ = State() #Состояние для ввода суммы накопления
    create_pb_descr = State() #Состояние для ввода орписания цели накопления
    save_up_more_pb = State() #состояние для отложения денег в копилку