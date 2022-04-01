import requests
from bs4 import BeautifulSoup

COOKIES = ""

def cookies_function(text):
    parts = text.split('; ')
    ans = {}
    for i in parts:
        ans[i.split('=', 1)[0]] = i.split('=', 1)[1]

    return ans


def get_page_html(keyword, page):
    url = f"https://publicwww.com/websites/{keyword}/{page}"

    headers = {
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'cache-control': "no-cache"
    }
    cookies = cookies_function(COOKIES)
    response = requests.request("GET", url, headers=headers, cookies=cookies)

    return response.text


def main(file_name, keyword, verbose=0, retry=None):
    if retry is None:
        retry = list(range(1, 51))

    temp_retry = []
    all_websites = []
    for i in retry:  # first 50 pages - 1000 website
        if i != 0:
            html = get_page_html(keyword, i)
            soup = BeautifulSoup(html, features='html.parser')
            found_websites = soup.find_all('a', {"rel": "noreferrer nofollow"})
            if verbose == 1:
                print(f"PAGE: {i}, {len(found_websites)} WEBSITE")

            if len(found_websites) == 0:
                temp_retry.append(i)
            else:
                for website in found_websites:
                    all_websites.append(website.get('href'))
    with open(f'{file_name}.csv', 'a', encoding='utf-8', newline='') as f:
        for website in all_websites:
            f.writelines(f'{website}\n')
    f.close()
    print(temp_retry)
    if len(temp_retry) > 0:
        return main(file_name, keyword, verbose=1, retry=temp_retry)


if __name__ == '__main__':
    keywords = ['notification', 'email', 'email newsletter']
    file_name = input('FILE NAME: ')
    for key in keywords:
        main(file_name, verbose=1, keyword=key)
