# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_urls(params):
    # Extract parameters from JSON input
    primary_category = params.get('Primary Category', '')
    secondary_category = params.get('Secondary Category', '')
    geography = params.get('Geography', '')
    date_range = params.get('Date Range', '')

    # Construct URL based on parameters (modify as per your target website structure)
    base_url = 'https://example.com/search'
    query_params = {
        'primary_category': primary_category,
        'secondary_category': secondary_category,
        'geography': geography,
        'date_range': date_range
    }
    response = requests.get(base_url, params=query_params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Assuming URLs are within <a> tags with specific class or structure, modify as per your target website
        urls = [link.get('href') for link in soup.find_all('a', class_='article-link')]

        return urls
    else:
        print(f"Failed to fetch URLs. Status code: {response.status_code}")
        return []

def save_to_csv(urls, output_file='output.csv'):
    # Save URLs to CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Primary Category', 'Secondary Category', 'Geography', 'Date Range'])  # CSV header
        for url in urls:
            writer.writerow([url, params['Primary Category'], params['Secondary Category'], params['Geography'], params['Date Range']])

    print(f"URLs saved to {output_file}")

if __name__ == "__main__":
    # Example JSON input (replace with your actual input)
    input_params = {
        "Primary Category": "Medical Journal",
        "Secondary Category": "Orthopedic",
        "Geography": "India",
        "Date Range": "2022"
    }

    # Fetch URLs based on input parameters
    urls = fetch_urls(input_params)

    # Save URLs to CSV file
    save_to_csv(urls)
