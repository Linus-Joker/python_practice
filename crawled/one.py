import requests as req
import bs4


def main():
    my_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept-Encoding": ""
    }

    for i in range(3):
        n = i+1
        url = "https://blog.moneydj.com/news/page/" + str(n)

        r = req.get(url, headers=my_headers, timeout=5)
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, 'html.parser')
            header = soup.find_all("header", class_="mh-loop-header")
            print("目前是第:", n, "頁")
            for h in header:
                title = h.find('h3', 'mh-loop-title').a.string
                print("標題:", title)


main()
