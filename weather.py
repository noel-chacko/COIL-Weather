# Import the necessary web scraping libraries
from bs4 import BeautifulSoup
import requests

# Print a simple line
print("COIL Ajman and Philly Collab")
print("Web Scraper is being set up...")

# Quick test to check if the libraries have been imported and are working
try:
    # Send a request to a simple website
    response = requests.get('https://example.com')

    # Parse the website content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the title of the webpage as a test
    print("Page title:", soup.title.string)
    
    print("Libraries imported and working successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
