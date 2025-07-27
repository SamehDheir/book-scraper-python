import requests
from bs4 import BeautifulSoup
import json

def fetch_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    book_list = []

    for book in books:
        title = book.h3.a.get("title", "No title")
        price = book.find("p", class_="price_color").text
        book_list.append({
            "title": title,
            "price": price
        })

    return book_list

def save_to_json(data, filename="books.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Data saved to {filename}")
    except IOError as e:
        print(f"File error: {e}")

def get_books():
    url = "https://books.toscrape.com/"
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    html = fetch_page(url, headers)
    if html:
        books = parse_books(html)
        save_to_json(books)

if __name__ == "__main__":
    get_books()
