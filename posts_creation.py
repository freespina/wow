import sqlite3

conn = sqlite3.connect('GEOshop.db')
c = conn.cursor()

conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')

conn.close()