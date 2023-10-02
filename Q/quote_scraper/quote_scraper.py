import requests
import os
from bs4 import BeautifulSoup


def fetch_quotes(url, num_pages=1):
    # Create a folder named 'quotes' if it doesn't exist
    if not os.path.exists("quotes"):
        os.makedirs("quotes")

    for page in range(1, num_pages + 1):
        response = requests.get(f"{url}/page/{page}/")
        if response.status_code != 200:
            print("Failed to retrieve the webpage.")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        quotes_divs = soup.find_all("div", class_="quote")

        print(f"--- Scraping Page {page} ---")

        for i, quote_div in enumerate(quotes_divs):
            quote = quote_div.find("span", class_="text").text
            author = quote_div.find("small", class_="author").text
            tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]

            print(f"Quote {i+1}: {quote}")
            print(f"Author: {author}")
            print(f"Tags: {tags}")
            print("-" * 50)

            author_folder = os.path.join("quotes", author.replace(" ", "_"))
            if not os.path.exists(author_folder):
                os.makedirs(author_folder)

            with open(f"{author_folder}/quote_{page}_{i+1}.txt", "w") as f:
                f.write(f"Quote: {quote}\n")
                f.write(f"Author: {author}\n")
                f.write(f"Tags: {', '.join(tags)}\n")


if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    num_pages = 10  # You can change this to scrape more or fewer pages
    fetch_quotes(url, num_pages)
