import sqlite3
from sqlite3 import Error

db_name = "LeetTrack.db"

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except Error as e:
        print(f"Database Error: {e}")
    return connection

def create_tables():
    connection = create_connection()

    if not connection:
        print("Could not establish a Database Connection!")
        return
    
    cursor = connection.cursor()

    # table for tacking problems
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            difficulty TEXT,
            topic TEXT,        
            status TEXT,             
            notes TEXT,
            date_added TEXT DEFAULT (DATE('now')),
            last_attempt TEXT
        )
    """)

    # extra table for tracking problem attempts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem_id INTEGER,
        date TEXT DEFAULT (DATE('now')),
        time_spent INTEGER,      
        result TEXT,           
        fail_reason TEXT,
        FOREIGN KEY (problem_id) REFERENCES problems (id)
    )
    """)

    connection.commit()
    connection.close()
    print("Database Tables have been successfully created!")

# main function
if __name__ == "__main__":
    create_tables()