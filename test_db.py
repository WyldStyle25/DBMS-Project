from database import get_connection

try:
    conn = get_connection()

    if conn.is_connected():
        print("SUCCESS! Connected to MySQL!")
        print("Database:", conn.database)

    conn.close()

except Exception as e:
    print("CONNECTION FAILED:", e)