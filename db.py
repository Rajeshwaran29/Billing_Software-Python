import pymysql

def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="2911",  # same password as test_db.py
            port=8080,
            database="tea_shop_db",
            cursorclass=pymysql.cursors.DictCursor  # fetch results as dicts
        )
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None
