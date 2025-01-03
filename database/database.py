import sqlite3 as sq3

def create_connection():
    """Создает соединение с БД"""
    try:
        conn = sq3.connect("./database_file/db.db3")
        return conn
    except sq3.Error as e:
        print(f"Ошибка при подключении к БД: {e}")
        return None

def load_db(id: int):
    """Создает таблицу для пользователя"""
    conn = create_connection()
    if conn:
      try:
          cur = conn.cursor()
          cur.execute(f"""CREATE TABLE IF NOT EXISTS User_{id}(
              type TEXT,
              summ INT,
              category TEXT,
              description TEXT,
              data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          )""")
          conn.commit()
      except sq3.Error as e:
         print(f"Ошибка при создании таблицы: {e}")
      finally:
          cur.close()
          conn.close()


def add_entry(id: int, entry_data: dict):
    """Добавляет запись (доход или расход) в таблицу пользователя"""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(f"""
                INSERT INTO User_{id} (type, summ, category, description)
                VALUES (?, ?, ?, ?)
            """, (entry_data['type'], int(entry_data['summ']), entry_data['category'], entry_data['description']))
            conn.commit()
        except sq3.Error as e:
             print(f"Ошибка при добавлении записи: {e}")
        finally:
             cur.close()
             conn.close()

def show_incomes(id: int, current_month: str):
    """Возвращает все доходы за этот месяц"""
    conn = create_connection()
    if conn:
        try:
            cur = conn.cursor()
            a = cur.execute(f"""
            SELECT summ, description, data FROM User_{id}
                WHERE strftime('%m', data) = ? AND type = 'Доход'
            """, (current_month, )
            ).fetchall()
        except sq3.Error as e:
            print(f'Ошибка при попытки получить доходы за текущий месяц: {e}')
        finally:
            cur.close()
            conn.close()
    return a

def show_wastes(id: int, current_month: str, category: str) -> list[tuple] | None:
    """Возвращает все расходы за этот месяц в выбранной категории"""
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        a = None # переменная a инициализируется значением None
        try:
            cur = conn.cursor()
            cur.execute(f"""
                SELECT summ, description, data FROM User_{id}
                WHERE strftime('%m', data) = ? AND category = ? AND type = 'Расход'
            """, (current_month, category)
            )
            a = cur.fetchall()
        except sq3.Error as e:
           print(f'Ошибка при попытки получить расходы за текущий месяц: {e}')
           return None
        finally:
            cur.close()
            conn.close()
    return a

def get_data_for_chart(id: int) -> list[tuple]:
    """
    Возвращает суммарные расходы по каждой категории за месяц
    """
    conn = create_connection()
    if conn:
        a = None
        cur = conn.cursor()
        try:
            cur.execute(f"""
            SELECT category, SUM(summ)
        FROM User_{id}
        WHERE strftime('%Y-%m', data) = strftime('%Y-%m', 'now') AND category != '-'
        GROUP BY category
        """
        )
            a = cur.fetchall()
        except sq3.Error as e:
            print(f'Ошибка при попытки получить расходы за текущий месяц: {e}')
            return None
        finally:
            cur.close()
            conn.close()

    return a
