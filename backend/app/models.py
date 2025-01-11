import sqlite3

DB_PATH = "store.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Product (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Comment (id INTEGER PRIMARY KEY, product_id INTEGER, user_id INTEGER, comment_text TEXT, sentiment TEXT, tags TEXT, cluster_id INTEGER, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    conn.close()


init_db()
