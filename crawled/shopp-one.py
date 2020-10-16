import requests as req
import bs4


def main():
    my_headers = {
        "user-agent": "Googlebot",
    }

    url = "https://shopee.tw/%E5%A4%96%E5%A5%97-cat.63.1533"

    r = req.get(url, headers=my_headers, allow_redirects=False)
    # print("status_code: ", r.status_code)
    if r.status_code == 200:
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        items = soup.find_all(
            "div",
            # class_="col-xs-2-4 shopee-search-item-result__item"
            class_="_1NoI8_ _16BAGk"
        )
        # print(len(items))
        # print(items)
        for i in items:
            title = i.string
            print("標題:", title)
    else:
        print(r.status_code, " status_code is not 200!!")


main()
