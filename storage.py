import sqlite3

DB_NAME_USUAL = "auction_base.db"
DB_NAME_USUAL = "auction_base_photos.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME_USUAL)
    conn.row_factory = sqlite3.Row
    return conn

class Storage():
    def __init__(self):
        self.create_table_if_not_exists()
    
    def create_table_if_not_exists(self):
        conn = get_db_connection()
        try:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        author TEXT,
                        bet INTEGER)
                """)
        finally:
            conn.close()

    def insert_data(self, name, bet):
        conn = get_db_connection()
        try: 
            with conn:
                conn.execute("""
                    INSERT INTO users (author, bet) VALUES (?, ?)
                """, (name, bet))
                conn.commit()
        finally:
            conn.close()


    def get_all_history(self):
        conn = get_db_connection()
        try:
            with conn:
                cursor = conn.execute("""
                    SELECT * FROM users
                    ORDER BY id DESC
                """)
                for row in cursor:
                    print(f"id: {row['id']}, author: {row['author']}, bet: {row['bet']}")
        finally:
            conn.close()

tabak = Storage()
#tabak.insert_data("john", 15000)
#tabak.insert_data("misha", 11000)
#tabak.insert_data("holo", 25000)

tabak.get_all_history()

