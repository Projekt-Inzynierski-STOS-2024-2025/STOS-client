import sqlite3

db_path = './cache/cache.db'

def setup_cache():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute(
        '''CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filepath TEXT,
                hash TEXT NOT NULL UNIQUE)
        ''')
    conn.commit()
    conn.close()

def drop_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    _ = cursor.execute('''DELETE FROM files''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_cache()
    drop_database()