tasks_db = []

def get_all_tasks(user_id: int):
    user_id= int(user_id)
    return tasks_db.get(user_id, [])

def add_task(user_id: int, title: str, deadline: str, chat_id: int):
    global _task_id_counter
    user_id= int(user_id)
    
    if user_id not in tasks_db:
        tasks_db[user_id] = []
        

    new_task = {
        "id": _task_id_counter,
        "user_id": user_id,
        "title": title,
        "deadline": deadline,
        "completed": False,
        "notified": False 
    }

    tasks_db[user_id].append(new_task)
    _task_id_counter +=1
    return new_task

def mark_task_completed(user_id: int,task_id: int):
    user_id = int(user_id)
    task_id = int(task_id)
    
    if user_id in tasks_db:
        for task in tasks_db[user_id]:
            if task["id"] == tasks_db:
                task["is_+completed"] = True
                return task
    return None

import sqlite3 
from datetime import datetime
DB_NAME = "todo_bot.db"
def init_db(): 
    with sqlite3.connect(DB_NAME) as conn: 
        cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
    ''')
    
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            deadline TEXT NOT NULL,          -- Формат: HH:MM
            is_completed BOOLEAN DEFAULT 0,  -- 0 - активна, 1 - выполнена
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    conn.commit()
    
    
def add_user(user_id: int, username: str): 
    with sqlite3.connect(DB_NAME) as conn: 
        cursor = conn.cursor() 
    cursor.execute( 
                   "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", 
                   (user_id, username) ) 
    conn.commit()
    
    
def add_task(user_id: int, title: str, deadline: str):
    with sqlite3.connect(DB_NAME) as conn: 
        cursor = conn.cursor() 
    cursor.execute( "INSERT INTO tasks (user_id, title, deadline) VALUES (?, ?, ?)", 
                   (user_id, title, deadline) ) 
    conn.commit()
    
    
def get_overdue_tasks():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M") 
    with sqlite3.connect(DB_NAME) as conn: 
        cursor = conn.cursor() # Выбираем задачи и ID пользователей для отправки уведомлений cursor.execute
        (''' SELECT user_id, title, 
         deadline FROM tasks WHERE is_completed = 0 AND deadline < ? ''', (now_str,)) 
        return cursor.fetchall()
