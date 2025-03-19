import sqlite3

# подключение к БД
def connect_db():
    return sqlite3.connect('besh_taxi.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS lan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        lan TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        name TEXT,
        phone TEXT, 
        ROLE TEXT
    )''')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS role(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       chat_id INTEGER,
       role TEXT
       )
       ''')


    conn.commit()
    conn.close()
# конец уподключение задача


# работа языком
def add_lan(chat_id, lan):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO lan (chat_id, lan) VALUES (?, ?) ON CONFLICT(chat_id) DO UPDATE SET lan = ?',
                   (chat_id, lan, lan))

    conn.commit()
    conn.close()

def find_lan(chat_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT lan FROM lan WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None

def change_lan(chat_id, lan):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('UPDATE lan SET lan = ? WHERE chat_id = ?',(lan, chat_id))
    conn.commit()
    conn.close()
# конец работы языком


# работа пользователем
def add_user(chat_id, phone, name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO users (chat_id, name, phone) VALUES (?, ?, ?) ON CONFLICT(chat_id) DO UPDATE SET name = ?, phone = ?',
        (chat_id, name, phone, name, phone))

    conn.commit()
    conn.close()

def find_user(chat_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()

    conn.close()
    return result
# конец работы пользователем


# работа с роль
def add_role(chat_id, role):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO roles (chat_id, role) VALUES (?, ?)
    ''',(chat_id, role))

def find_role(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM roles WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def change_role(chat_id, role):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE roles SET role = ? WHERE chat_id = ?', (role, chat_id))
# конец работ с ролем


# работа поездка
def add_trip(chat_id, name, driver_chat_id):
    pass

def find_trip(chat_id):
    pass

# конец работы поездки


# Создаем таблицы при запуске скрипта
create_tables()