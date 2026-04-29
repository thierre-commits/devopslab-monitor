import time
import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

for i in range(10):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        print("Database is ready!")
        break
    except Exception:
        print("Waiting for database...")
        time.sleep(2)
else:
    raise Exception("Database not ready after retries")
