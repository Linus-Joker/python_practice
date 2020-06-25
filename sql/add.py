import mysql.connector
from mysql.connector import Error

try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='localhost',       # 主機名稱
        database='test',        # 資料庫名稱
        user='root',            # 帳號
        password='')  # 密碼

    # 新增資料
    sql = "INSERT INTO tb (title) VALUES (%s);"
    title = ("new day",)
    cursor = connection.cursor()
    cursor.execute(sql, title)

    # 確認資料有存入資料庫
    connection.commit()

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
