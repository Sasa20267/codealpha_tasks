import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
max_pages = 50

data = []

for page in range(1, max_pages + 1):
    page_url = base_url.format(page)

    response = None
    for attempt in range(3):
        try:
            response = requests.get(page_url, timeout=10)
            break
        except requests.exceptions.RequestException:
            print("Page", page, "attempt", attempt + 1, "failed, retrying...")
            time.sleep(2)
    if response is None:
        print("Giving up on page", page)
        continue

    response.encoding = "utf-8"
    print("Page", page, "status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating_word = book.find("p", class_="star-rating")["class"][1]
        rating = rating_map[rating_word]
        availability = book.find("p", class_="availability").text.strip()
        product_url = urljoin(page_url, book.h3.a["href"])
        data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "product_url": product_url,
        })

    time.sleep(0.5)

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print(df.shape)
print(df.head())