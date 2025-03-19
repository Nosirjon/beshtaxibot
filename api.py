from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("besh_taxi.db")
    conn.row_factory = sqlite3.Row
    return conn

# Создание таблицы, если её нет
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        from_region TEXT,
        to_region TEXT
    )
''')
conn.commit()
conn.close()

class UserData(BaseModel):
    name: str
    phone: str
    from_region: str
    to_region: str

@app.post("/submit/")
def submit_form(data: UserData):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, phone, from_region, to_region) VALUES (?, ?, ?, ?)",
                   (data.name, data.phone, data.from_region, data.to_region))
    conn.commit()
    conn.close()
    return {"message": "Данные успешно сохранены!"}
