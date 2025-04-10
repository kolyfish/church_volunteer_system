import sqlite3


def check_tables():
    db_file = '../database/church.db'

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 從 sqlite_master 查詢所有存在的表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("成功建立以下資料表:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("未找到任何資料表，檢查程式是否成功創建表！")

        conn.close()
    except Exception as e:
        print(f"檢查資料表時發生錯誤: {e}")


check_tables()
