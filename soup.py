# Import the required libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Provide the URL of the website
url = "https://www.w3schools.com/python/python_datatypes.asp"  # Replace with the website you want to scrape

# Step 2: Fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Webpage fetched successfully!\n")
    
    # Step 3: Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 4: Extract and display all paragraphs (<p> tags)
    print("Paragraphs found on the webpage:\n")
    paragraphs = soup.find_all('p')  # Find all <p> tags
    for i, paragraph in enumerate(paragraphs, start=1):
        print(f"Paragraph {i}: {paragraph.text.strip()}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
