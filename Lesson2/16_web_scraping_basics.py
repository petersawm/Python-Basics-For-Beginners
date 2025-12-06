# Web Scraping Basics - Extracting data from websites
# Install required libraries: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Basic web scraping example
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None

# Parse HTML content
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# Example: Scraping a simple webpage
def scrape_example():
    url = "http://quotes.toscrape.com/"
    
    html = fetch_webpage(url)
    if not html:
        return
    
    soup = parse_html(html)
    
    # Find all quotes
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    print("--- Quotes ---\n")
    for quote, author in zip(quotes, authors):
        print(f'"{quote.text}"')
        print(f"- {author.text}\n")

# scrape_example()

# Finding elements by different selectors
def find_elements_example(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find by tag name
    title = soup.find('h1')
    
    # Find by class
    items = soup.find_all('div', class_='item')
    
    # Find by id
    header = soup.find(id='header')
    
    # Find all links
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
    
    # CSS selectors
    results = soup.select('.container > div')

# Scraping with headers (act like a real browser)
def scrape_with_headers(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error: {e}")
        return None

# Extract specific data
def scrape_product_prices(url):
    soup = scrape_with_headers(url)
    if not soup:
        return
    
    # Example: Find all products
    products = soup.find_all('div', class_='product')
    
    for product in products:
        name = product.find('h2').text
        price = product.find('span', class_='price').text
        print(f"{name}: {price}")

# Scraping tables
def scrape_table(url):
    html = fetch_webpage(url)
    if not html:
        return
    
    soup = parse_html(html)
    table = soup.find('table')
    
    if table:
        rows = table.find_all('tr')
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = [cell.text.strip() for cell in cells]
            print(row_data)

# Handling pagination
def scrape_multiple_pages(base_url, num_pages):
    all_data = []
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}...")
        
        html = fetch_webpage(url)
        if html:
            soup = parse_html(html)
            # Extract data from this page
            items = soup.find_all('div', class_='item')
            all_data.extend(items)
        
        # Be respectful - wait between requests
        import time
        time.sleep(1)
    
    return all_data

# Extracting specific attributes
def extract_links(url):
    html = fetch_webpage(url)
    if not html:
        return
    
    soup = parse_html(html)
    links = soup.find_all('a')
    
    print("--- All Links ---")
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href:
            print(f"{text}: {href}")

# Extracting images
def extract_images(url):
    html = fetch_webpage(url)
    if not html:
        return
    
    soup = parse_html(html)
    images = soup.find_all('img')
    
    print("--- All Images ---")
    for img in images:
        src = img.get('src')
        alt = img.get('alt', 'No description')
        print(f"{alt}: {src}")

# Download an image
def download_image(image_url, filename):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Image downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Cleaning scraped text
def clean_text(text):
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Remove special characters if needed
    return text.strip()

# Save scraped data to file
def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(str(item) + '\n')
    print(f"Data saved to {filename}")

# Save to CSV
def save_to_csv(data, filename):
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Rating'])  # Headers
        
        for item in data:
            writer.writerow([item['title'], item['price'], item['rating']])
    
    print(f"Data saved to {filename}")

# Practical example: News headline scraper
def scrape_headlines(url):
    soup = scrape_with_headers(url)
    if not soup:
        return
    
    headlines = soup.find_all('h2', class_='headline')
    
    print("--- Latest Headlines ---\n")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline.text.strip()}")

# Error handling in scraping
def safe_scrape(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find specific elements
        title = soup.find('h1')
        if title:
            print(f"Title: {title.text}")
        else:
            print("Title not found")
        
    except requests.Timeout:
        print("Request timed out")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Respecting robots.txt
def check_robots_txt(base_url):
    robots_url = f"{base_url}/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            print(response.text)
    except Exception as e:
        print(f"No robots.txt found: {e}")

# Complete scraper example
class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_page(self, path=''):
        url = self.base_url + path
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_data(self, soup, selector):
        if soup:
            return soup.select(selector)
        return []
    
    def scrape_and_save(self, selector, filename):
        soup = self.fetch_page()
        if soup:
            elements = self.extract_data(soup, selector)
            
            with open(filename, 'w', encoding='utf-8') as file:
                for element in elements:
                    file.write(element.text.strip() + '\n')
            
            print(f"Scraped {len(elements)} items to {filename}")

# Usage example
# scraper = WebScraper("http://example.com")
# scraper.scrape_and_save('.article-title', 'articles.txt')

# Important notes about web scraping:
"""
1. Always check robots.txt before scraping
2. Add delays between requests (time.sleep())
3. Use headers to identify your scraper
4. Respect website's terms of service
5. Don't overload servers with too many requests
6. Cache results when possible
7. Handle errors gracefully
8. Some websites require authentication
9. Dynamic content may need Selenium (JavaScript)
10. Always verify data accuracy
"""

# Rate limiting example
import time

def rate_limited_scraper(urls, delay=2):
    results = []
    
    for i, url in enumerate(urls, 1):
        print(f"Scraping {i}/{len(urls)}...")
        
        html = fetch_webpage(url)
        if html:
            soup = parse_html(html)
            # Process soup here
            results.append(soup)
        
        # Wait between requests
        if i < len(urls):
            time.sleep(delay)
    
    return results