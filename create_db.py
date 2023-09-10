import sqlite3

def create_db():
    con=sqlite3.connect(database=r"ngg.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(uid INTEGER PRIMARY KEY AUTOINCREMENT,username text, email text, password text, created_at DATETIME DEFAULT CURRENT_TIMESTAMP )")
    con.commit()

create_db()

