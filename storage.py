import sqlite3
import random

DB_NAME_USUAL = "auction_base.db"


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
                        name TEXT UNIQUE,
                        bet INTEGER)
                """)
        finally:
            conn.close()

    def insert_data(self, name, bet):
        conn = get_db_connection()
        try: 
            with conn:
                conn.execute("""
                    INSERT INTO users (name, bet) VALUES (?, ?)
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
                    ORDER BY bet DESC
                """)
                for row in cursor:
                    print(f"id: {row['id']}, name: {row['name']}, bet: {row['bet']}")
        finally:
            conn.close()
    
    def get_update_bet(self, name, bet):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql_update = """UPDATE users SET bet = ? WHERE name = ? AND bet < ?"""
        try:
            
            with conn:
                cursor.execute(sql_update, (bet, name, bet))
                conn.commit()
                if cursor.rowcount > 0:
                    print(f"Success! bet was updated to {bet}")
                else:
                    print(f"Fail :(    your new bet {bet} less then old ")
        finally:
            conn.close()



tabak = Storage()
print("Name, your bet")
for i in range(random.randint(1,5)):
    name = input("Enter ur name: ")
    bet = int(input("Enter your bet: "))
    tabak.insert_data(name, bet)


tabak.get_all_history()
print("update your bet")
name = input("Enter ur name: ")
bet = int(input("Enter your bet: "))
tabak.get_update_bet(name, bet)
tabak.get_all_history()
