import pymysql
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",       # or 127.0.0.1
            user="root",            # your MySQL username
            password="2911",
            port=8080,# your MySQL password
            database="tea_shop_db"
        )
        print("✅ Database connected successfully!")
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)
