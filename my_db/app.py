import sqlite3


# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ny_db.db')
cursor = conn.cursor()

# Step 1: Create the 'students' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

# Step 2: Insert some student records
students_data = [
    ("Ali Raza", "ali.raza@example.com"),
    ("Sana Tariq", "sana.tariq@example.com"),
    ("Hamza Khan", "hamza.khan@example.com"),
    ("Zara Ahmed", "zara.ahmed@example.com")
]

cursor.executemany("INSERT INTO students (name, email) VALUES (?, ?)", students_data)

# Commit changes and close the connection
conn.commit()
conn.close()