import sqlite3

conn = sqlite3.connect('GEOshop.db')
c = conn.cursor()

# Create database users
conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')

# Add column operation
try:
    conn.execute("ALTER TABLE posts ADD COLUMN short_description TEXT NOT NULL DEFAULT ''")
except sqlite3.OperationalError:
    pass

# Create user
conn.execute('''
    INSERT INTO users (username, email, age) VALUES ('Misho gatenashvili', 'orinabijisparki@gmail.com', 23)
''')
conn.commit()

# Update user
conn.execute('''
    UPDATE users SET password = '12341234' WHERE email = 'orinabijisparki@gmail.com'
''')
conn.commit()

# Delete operation
conn.execute('''
    DELETE FROM users WHERE id = 1
''')
conn.commit()

# Read operation
c.execute('SELECT id, username FROM users')
rows = c.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}")


conn.close()