import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def fetch_page(url, proxies=None):
    for attempt in range(3):
        try:
            response = requests.get(url, proxies=proxies, timeout=10)
            response.raise_for_status()
            return response.text
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5) 
    return None

def scrape_products(url, proxies=None):
    page_content = fetch_page(url, proxies)
    if not page_content:
        print("Error fetching the webpage.")
        return []

    soup = BeautifulSoup(page_content, 'html.parser')
    products = []

    product_elements = soup.select('.product-item')

    for product in product_elements:
        title = product.select_one('.product-title').get_text(strip=True)
        price = product.select_one('.price').get_text(strip=True)
        brand = product.select_one('.brand-name').get_text(strip=True)
        seller = product.select_one('.seller-name').get_text(strip=True)

        products.append({
            'title': title,
            'price': price,
            'brand': brand,
            'seller': seller
        })

    return products

def main():
    url = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
    
    proxies = {
        "http": "http://138.201.23.100:3128",
        "https": "http://138.201.23.100:3128",
    }
    
    products = scrape_products(url, proxies)
    if products:
        df = pd.DataFrame(products)
        df.to_csv('noon_yoga_products.csv', index=False)
        print(f"Scraped {len(products)} products and saved to noon_yoga_products.csv")

if __name__ == "__main__":
    main()
