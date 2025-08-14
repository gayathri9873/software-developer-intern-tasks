import requests
from bs4 import BeautifulSoup
import csv

# Example website for safe practice
url = "https://books.toscrape.com/"

# Send HTTP request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
products = soup.find_all("article", class_="product_pod")

# Create a CSV file to save product data
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating"])  # CSV header

    # Extract information for each product
    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.p["class"][1]  # Example: 'Three', 'Five'
        writer.writerow([name, price, rating])

print("Product data has been saved to products.csv")

