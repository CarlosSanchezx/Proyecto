import sqlite3

def create_database():
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            coins INTEGER DEFAULT 0,
            level INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

create_database()