import requests
from bs4 import BeautifulSoup

# Convert star rating word to number
def get_rating_value(rating_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)

# Target URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book items
books = soup.find_all("article", class_="product_pod")

# Extract data
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating_class = book.find("p", class_="star-rating")["class"][1]
    rating = get_rating_value(rating_class)

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating} stars")
    print("-" * 40)
