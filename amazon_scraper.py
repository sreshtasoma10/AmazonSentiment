
import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119 Safari/537.36"
}

def extract_reviews(url, max_pages=3):
    reviews = []
    for page in range(1, max_pages + 1):
        page_url = f"{url}&pageNumber={page}"
        html = requests.get(page_url, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")
        review_blocks = soup.find_all("span", {"data-hook": "review-body"})
        for block in review_blocks:
            text = block.get_text(strip=True)
            reviews.append(text)
    return reviews
