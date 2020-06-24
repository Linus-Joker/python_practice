import requests as req
import bs4


def main():
    url = "https://blog.moneydj.com/news"

    my_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    }
    for i in range(3):
        payload = {
            'key': i
        }
        r = req.get(url, headers=my_headers, timeout=5, params=payload)
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, 'html.parser')
            header = soup.find_all("header", class_="mh-loop-header")

            for h in header:
                title = h.find('h3', 'mh-loop-title').a.string
                print("標題:", title)


main()
