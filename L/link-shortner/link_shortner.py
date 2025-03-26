import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "https://short.url/"

    def shorten_url(self, original_url):
        # Generate a unique identifier for the URL using MD5 hash
        md5_hash = hashlib.md5(original_url.encode()).hexdigest()
        
        # Take the first 8 characters of the hash as the short URL
        short_url = md5_hash[:8]
        
        # Store the mapping between the short URL and the original URL
        self.url_mapping[short_url] = original_url
        return self.base_url + short_url

    def expand_url(self, short_url):
        # Extract short key from URL
        short_key = short_url.split("/")[-1]
        
        # Look up original URL from mapping
        original_url = self.url_mapping.get(short_key, None)
        return original_url

# Usage
if __name__ == "__main__":
    url_shortener = URLShortener()
    original_url = "https://www.example.com"
    short_url = url_shortener.shorten_url(original_url)
    print(f"Short URL: {short_url}")
    expanded_url = url_shortener.expand_url(short_url)
    print(f"Expanded URL: {expanded_url}")

