IN_DB =[] #Список пользователей, для которых создана база данных
entry_data = {} #словарь для проежуточного сохранения данных
pb = {}
Piggi_bank = {
    'goal_summ': 0 , #по умолчанию нет цели
    'is_goal': False, #есть ли цель, если нету, то скрипт с откладыванием денег не работает
    'summa': 0, #Сумма денег в копилке сейчас
    'goal_descr': ' ' #Описание цели накопления
}
user_balances = {}