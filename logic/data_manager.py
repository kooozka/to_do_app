import sqlite3, datetime, logic.task_manager as task_manager
from logic.task_manager import Task

class DatabaseConfig:
        DATABASE_NAME = "todoapp_db"

def create_database():
        conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)

        c = conn.cursor()
        c.execute('''
                CREATE TABLE Tasks (
                task_id INTEGER PRIMARY KEY,
                title TEXT,
                category INTEGER,
                description TEXT,
                priority INTEGER,
                deadline DATE,
                completed INTEGER,
                user_login TEXT,
                FOREIGN KEY (user_login) REFERENCES Users(login))''')
        
        c.execute('''
                CREATE TABLE Users (
                login TEXT PRIMARY KEY,
                password TEXT
                )
        ''')
        c.execute("INSERT INTO Users (login, password) VALUES (?, ?)",
              ("ADMINISTRATOR", "123"))
        conn.commit()
        conn.close()

def add_task(title: str, category, description: str, priority, deadline: datetime, login: str):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor() 
    c.execute("INSERT INTO Tasks (title, category, description, priority, deadline, user_login) VALUES (?, ?, ?, ?, ?, ?)",
              (title, category, description, priority, deadline, login))
    conn.commit()
    conn.close()

def add_user(login: str, password: str):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor() 
    #c.execute("SELCT * FROM Users WHERE login = ?", (login,))
    #user = c.fetchall()
    #if not user:
    c.execute("INSERT INTO Users (login, password) VALUES (?, ?)",
              (login, password))
    conn.commit()
    conn.close()

def login_success(login: str, password: str):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor() 
    c.execute("SELECT * FROM Users WHERE login = ? AND password = ?", (login, password))
    result = c.fetchone()
    conn.commit()
    conn.close()
    if result:
         return True
    return False

def get_tasks():
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM Tasks")
    db_tasks = c.fetchall()
    conn.commit()
    conn.close()
    tasks = []
    for db_task in db_tasks:
          task = Task(db_task[0], db_task[1], task_manager.Categories(db_task[2]), db_task[3], task_manager.Priority(db_task[4]), db_task[5], db_task[7])
          tasks.append(task)
    return tasks

def get_user_tasks(login):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM Tasks WHERE user_login = ?", (login,))
    db_tasks = c.fetchall()
    conn.commit()
    conn.close()
    tasks = []
    for db_task in db_tasks:
          task = Task(db_task[0], db_task[1], task_manager.Categories(db_task[2]), db_task[3], task_manager.Priority(db_task[4]), db_task[5], db_task[6])
          tasks.append(task)
    return tasks


def remove_task(task_id):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM Tasks WHERE task_id = ?", (task_id,))  
    conn.commit()
    conn.close()

def update_task(id, title: str, category, description: str, priority, deadline: datetime, login: str):
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE Tasks SET title = ?, category = ?, description = ?, priority = ?, deadline = ?, user_login = ? WHERE task_id = ?",
              (title, category, description, priority, deadline, login, id))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DatabaseConfig.DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT login FROM Users")  
    logins = c.fetchall()
    conn.commit()
    conn.close()
    return [login[0] for login in logins if login[0] != "ADMINISTRATOR"]
