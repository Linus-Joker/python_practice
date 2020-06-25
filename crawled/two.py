import requests as req
import bs4
import mysql.connector
from mysql.connector import Error


def main():
    try:
        # 連接 MySQL/MariaDB 資料庫
        connection = mysql.connector.connect(
            host='localhost',       # 主機名稱
            database='test',        # 資料庫名稱
            user='root',            # 帳號
            password='')            # 密碼

        # 好像是連接
        sql = "INSERT INTO tb (title) VALUES (%s);"
        cursor = connection.cursor()

        # 標頭檔
        my_headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
            "Accept-Encoding": ""
        }

        # 開始
        for i in range(3):
            n = i+1
            url = "https://blog.moneydj.com/news/page/" + str(n)

            r = req.get(url, headers=my_headers, timeout=5)
            if r.status_code == 200:
                soup = bs4.BeautifulSoup(r.text, 'html.parser')
                header = soup.find_all("header", class_="mh-loop-header")

                for h in header:
                    new_title = h.find('h3', 'mh-loop-title').a.string
                    title = (str(new_title),)
                    cursor.execute(sql, title)
                    # print("標題:", new_title)

                    # 確認資料有存入資料庫
                    connection.commit()
    except Error as e:
        print("資料庫連接失敗：", e)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


main()
