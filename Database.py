import sqlite3

conn =sqlite3.connect('chatbot.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS intents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_message TEXT,
    bot_response TEXT,
    intent TEXT,         
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
print("Database and table created successfully.")

                                     
conn.commit()
conn.close()
               