import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

home_url = "https://books.toscrape.com/"


def get_page(url):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "utf-8"
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException:
            print("Failed, retrying:", url)
            time.sleep(2)
    return None


def get_category_book_urls(category_url):
    book_urls = []
    page_url = category_url
    while page_url:
        soup = get_page(page_url)
        if soup is None:
            print("Giving up on", page_url)
            break
        for book in soup.find_all("article", class_="product_pod"):
            book_urls.append(urljoin(page_url, book.h3.a["href"]))
        next_button = soup.find("li", class_="next")
        if next_button:
            page_url = urljoin(page_url, next_button.a["href"])
        else:
            page_url = None
        time.sleep(0.5)
    return book_urls


soup = get_page(home_url)
links = soup.find("div", class_="side_categories").find("ul").find("ul").find_all("a")

categories = []
for a in links:
    name = a.text.strip()
    category_url = urljoin(home_url, a["href"])
    categories.append({"name": name, "url": category_url})

rows = []
for category in categories:
    urls = get_category_book_urls(category["url"])
    print(category["name"], len(urls))
    for u in urls:
        rows.append({"product_url": u, "category": category["name"]})

category_df = pd.DataFrame(rows)
category_df.to_csv("category_map.csv", index=False, encoding="utf-8-sig")

print(category_df.shape)