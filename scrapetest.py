import requests
from bs4 import BeautifulSoup
import csv

# URL of the target page
url = 'https://www.scrapethissite.com/pages/simple/'

# Send a GET request to the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all country containers
countries = soup.find_all('div', class_='col-md-4 country')

# Open a CSV file to write the data
with open('countries.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Name', 'Capital', 'Population', 'Area'])
    
    # Iterate through each country and extract details
    for country in countries:
        name = country.find('h3', class_='country-name').get_text(strip=True)
        capital = country.find('span', class_='country-capital').get_text(strip=True)
        population = country.find('span', class_='country-population').get_text(strip=True)
        area = country.find('span', class_='country-area').get_text(strip=True)
        # Write the data row
        writer.writerow([name, capital, population, area])
