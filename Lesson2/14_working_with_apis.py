# Working with APIs - fetching data from the internet
# Note: You need to install 'requests' library first
# Run: pip install requests

import requests
import json

# Basic GET request
# Example with a free API
url = "https://api.github.com/users/github"

try:
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Username: {data['login']}")
        print(f"Name: {data['name']}")
        print(f"Public Repos: {data['public_repos']}")
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

# Working with JSONPlaceholder (free fake API for testing)
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        # Show first 5 posts
        for post in posts[:5]:
            print(f"\nTitle: {post['title']}")
            print(f"Body: {post['body'][:50]}...")
    else:
        print("Failed to fetch posts")

# get_posts()

# GET request with parameters
def search_repositories(query):
    url = "https://api.github.com/search/repositories"
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc'
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total_count']} repositories")
        
        for repo in data['items'][:5]:
            print(f"\n{repo['name']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")
    else:
        print(f"Error: {response.status_code}")

# search_repositories("python")

# POST request - creating data
def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        'title': 'My Test Post',
        'body': 'This is the content',
        'userId': 1
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 201:  # 201 = Created
        result = response.json()
        print("Post created successfully!")
        print(f"ID: {result['id']}")
        print(f"Title: {result['title']}")
    else:
        print("Failed to create post")

# create_post()

# PUT request - updating data
def update_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    data = {
        'title': 'Updated Title',
        'body': 'Updated content',
        'userId': 1
    }
    
    response = requests.put(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Post updated successfully!")
        print(result)
    else:
        print("Failed to update post")

# update_post(1)

# DELETE request
def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully!")
    else:
        print("Failed to delete post")

# delete_post(1)

# Working with headers
def get_with_headers():
    url = "https://api.github.com/users/github"
    headers = {
        'User-Agent': 'My Python App',
        'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(data['login'])

# Timeout handling
def fetch_with_timeout(url):
    try:
        response = requests.get(url, timeout=5)  # 5 seconds timeout
        return response.json()
    except requests.Timeout:
        print("Request timed out")
    except requests.RequestException as e:
        print(f"Error: {e}")
    return None

# Weather API example (requires API key from OpenWeatherMap)
def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Note: You need to get a free API key from openweathermap.org
# get_weather("London", "YOUR_API_KEY")

# Practical example - Quote fetcher
def get_random_quote():
    url = "https://api.quotable.io/random"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n\"{data['content']}\"")
            print(f"- {data['author']}")
        else:
            print("Failed to fetch quote")
    except Exception as e:
        print(f"Error: {e}")

# get_random_quote()

# Saving API response to file
def save_api_data(url, filename):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(filename, 'w') as file:
                json.dump(response.json(), file, indent=2)
            print(f"Data saved to {filename}")
        else:
            print("Failed to fetch data")
    except Exception as e:
        print(f"Error: {e}")

# save_api_data("https://jsonplaceholder.typicode.com/posts/1", "post_data.json")

# Reading saved API data
def load_api_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON file")
        return None

# Error handling best practices
def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises exception for bad status codes
        
        data = response.json()
        return data
        
    except requests.ConnectionError:
        print("Connection error. Check your internet.")
    except requests.Timeout:
        print("Request timed out")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None

# user = fetch_user_data(1)
# if user:
#     print(user['name'])

# Rate limiting - being respectful to APIs
import time

def fetch_multiple_users(user_ids):
    users = []
    for user_id in user_ids:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            users.append(response.json())
        
        time.sleep(0.5)  # Wait 0.5 seconds between requests
    
    return users

# users = fetch_multiple_users([1, 2, 3, 4, 5])
# for user in users:
#     print(user['name'])

# Simple API wrapper class
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None

# Using the wrapper
# client = APIClient("https://jsonplaceholder.typicode.com")
# posts = client.get("posts")
# if posts:
#     print(f"Fetched {len(posts)} posts")