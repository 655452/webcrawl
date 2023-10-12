# http://127.0.0.1:5500/index.html

import requests
from bs4 import BeautifulSoup
import csv

# Make an HTTP request
response = requests.get('https://unsplash.com/s/photos/food-photography')
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract image URLs
    image_urls = [img['src'] for img in soup.find_all('img')]

# Save image URLs to a CSV file
with open('image_urls2.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for url in image_urls:
        csv_writer.writerow([url])
