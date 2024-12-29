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
              description TEXT
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
