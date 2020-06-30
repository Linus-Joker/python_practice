import requests as req
import bs4


def main():
    my_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept-Encoding": ""
    }
    url = "https://www.ptt.cc/bbs/NBA/index.html"
    r = req.get(url, timeout=5)
    # print(r.status_code)
    if r.status_code == 200:
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        print("標題:", soup.title.string)
    else:
        print("status_code is not 200!!")


main()
