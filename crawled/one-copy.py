import requests as req
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


def main():
    my_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept-Encoding": ""
    }

    url = "https://www.ptt.cc/bbs/NBA/index.html"

    r = req.get(url, headers=my_headers, timeout=5)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        author_ids = []  # 建立一個空的 list 來放作者 id
        recommends = []  # 建立一個空的 list 來放推文數
        post_titles = []  # 建立一個空的 list 來放文章標題
        post_dates = []  # 建立一個空的 list 來放發文日期

        posts = soup.find_all("div", class_="r-ent")
        for post in posts:
            try:
                author_ids.append(post.find("div", class_="author").string)
            except:
                author_ids.append(np.nan)
            try:
                post_titles.append(post.find("a").string)
            except:
                post_titles.append(np.nan)
            try:
                post_dates.append(post.find("div", class_="date").string)
            except:
                post_dates.append(np.nan)

        # 推文數藏在 div 裡面的 span 所以分開處理
        recommendations = soup.find_all("div", class_="nrec")
        for recommendation in recommendations:
            try:
                recommends.append(int(recommendation.find("span").string))
            except:
                recommends.append(np.nan)

        ptt_nba_dict = {"author": author_ids,
                        "recommends": recommends,
                        "title": post_titles,
                        "date": post_dates
                        }

        ptt_nba_df = pd.DataFrame(ptt_nba_dict)
        print(ptt_nba_df)


main()
