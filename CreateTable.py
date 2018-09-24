import sqlite3

DATABASE = 'DRAFT.db'
conn = sqlite3.connect(DATABASE)

def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS currentUsers
             (id INTEGER PRIMARY KEY,
              user_id INTEGER,
              age TEXT,
              under_consideration_count INTEGER,
              rank TEXT,
              past_amount INTEGER,
              ambition TEXT,
              tech_list TEXT
              )'''
    conn.execute(sql)
    conn.commit()
    conn.close()
    
create_table()
