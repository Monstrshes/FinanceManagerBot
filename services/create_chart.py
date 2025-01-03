import matplotlib.pyplot as plt
import os

def generate_pie_chart(id: int, expenses: list[tuple]):
    """Создает круговую диаграмму и сохраняет ее в файл."""


    if not expenses:
        return None  # Нет данных для диаграммы

    categories = [row[0] for row in expenses]
    amounts = [row[1] for row in expenses]

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Расходы за текущий месяц')
    plt.axis('equal')  # Чтобы диаграмма была круглой

    chart_path = f'./temporary_files/monthly_expenses_{id}.png'  # Путь к файлу для сохранения
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def del_chart(pie_chart):
    os.remove(path=pie_chart)