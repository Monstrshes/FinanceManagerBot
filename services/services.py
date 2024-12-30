from datetime import datetime

#Возвращает текущий месяц
def get_now_month() -> datetime:
    current_month=  datetime.now().month
    return f"{current_month:02d}"

#Возвращает сумму доходов или расходов
def summ_incomes_or_wastes(lst: list):
    counter = 0
    for a in lst:
        counter += a[0]
    return counter

#Из списка от базы данных создаем словраь обработки инлайн кнопок
def create_sl_from_incomes_db(lst: list) -> dict:
    sl_for_inline = {}
    for item in lst:
        sl_for_inline[f'{item[0]}_{item[2]}'] = [item[2], item[1]]
    return sl_for_inline
