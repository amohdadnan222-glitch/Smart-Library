import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Change this to your actual admin password
plain_password = "admin123"

hashed_password = generate_password_hash(plain_password)

cursor.execute(
    """
    UPDATE admin
    SET password=?
    WHERE username=?
    """,
    (
        hashed_password,
        "admin"
    )
)

conn.commit()
conn.close()

print("Admin password hashed successfully!")