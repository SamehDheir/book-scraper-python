# 📚 Book Scraper

A simple Python project that scrapes book titles and prices from [Books to Scrape](https://books.toscrape.com) and saves the data into a JSON file.

This project is intended for learning and practicing web scraping using **requests**, **BeautifulSoup**, and **JSON** handling in Python.

---

## 🚀 Features

- Fetches the homepage of books.toscrape.com
- Parses book titles and prices
- Saves the extracted data in a clean JSON format
- Basic error handling for requests and file saving

---

## 🛠️ Tech Stack

- Python 3
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- JSON module (built-in)

---

## 📦 Output

The scraped data is saved to a file called `books.json`:

```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77"
  },
  ...
]
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-scraper.git
   cd book-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python scraper.py
   ```

---

## 📚 About the Website

[books.toscrape.com](https://books.toscrape.com) is a sandbox website designed for practicing web scraping. It is safe and legal to scrape.

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/sameh-dheir/) or check out my other projects on [GitHub](https://github.com/SamehDheir)

---

## 🏷️ License

This project is for educational use only.
