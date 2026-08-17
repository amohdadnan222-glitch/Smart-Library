import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Add due_date column
try:
    cursor.execute("""
    ALTER TABLE issued_books
    ADD COLUMN due_date TEXT
    """)
    print("✓ due_date column added")
except sqlite3.OperationalError as e:
    print("due_date:", e)

# Add fine column
try:
    cursor.execute("""
    ALTER TABLE issued_books
    ADD COLUMN fine INTEGER DEFAULT 0
    """)
    print("✓ fine column added")
except sqlite3.OperationalError as e:
    print("fine:", e)

conn.commit()
conn.close()

print("Database updated successfully!")