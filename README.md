# 🕷️ Web Scraper

## 📖 Project Description

This is a simple backend web scraping project built with Python. It collects data from a target website and stores the extracted information in a CSV file for further analysis or use.

The project is designed for learning and experimenting with basic web scraping techniques using libraries like `requests` and `BeautifulSoup`.

---

## 🛠️ Requirements

Make sure you have Python installed. Then install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Run

1. Open the file `scraper.py`.
2. Set the target URL and adjust the scraping logic as needed.
3. Run the script:

```bash
python scraper.py
```

4. The scraped data will be saved in `output.csv`.

---

## 🧰 Technologies Used

- **Python 3**
- `requests` – for sending HTTP requests
- `BeautifulSoup` – for parsing and navigating HTML

---

## 📁 Project Structure

```
web_scraper/
│
├── scraper.py        # Main script for scraping
├── output.csv        # Extracted data (auto-generated)
└── README.md         # Project description and usage
```

---

## ⚠️ Notes

- Always check the target website’s `robots.txt` file to ensure scraping is allowed.
- Avoid sending too many requests in a short time to prevent getting blocked.
- This project is for educational purposes only.
