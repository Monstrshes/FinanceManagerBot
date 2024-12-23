#Файл для создания машины сосотояний


from aiogram.fsm.state import  State, StatesGroup

class FSMFillForm(StatesGroup):
    menu = State()

    to_income = State() #Состояние после нажатия из меню кнопки к доходам
    append_income = State() #Состояние для добавленрия дохода
    show_income  = State() #Состояние для просмотра доходов
    input_income = State() #Состояние для ввода дохода как числа
    input_description = State() ##Состояние для ввода описания дохода

    to_waste = State() #Состояние после нажатия из меню кнопки к расходам
    choose_category = State() #Состояние для выбора для добавления расхода
    append_waste = State() #Состояние для добавления расходов
    show_waste = State() #Состояние для просмотра расходов
    input_waste = State() #Состояние для ввода расхода как числа
    input_waste = State() ##Состояние для ввода описания расхода

    other = State() #Состояние после нажатия из менб кнопки Другое
