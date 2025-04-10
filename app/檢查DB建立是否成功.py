import os

db_file = 'database/church.db'
if os.path.exists(db_file):
    print(f"資料庫已成功建立在: {db_file}")
else:
    print("資料庫檔案未建立！")
