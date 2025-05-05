import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the target page
url = 'https://www.scrapethissite.com/pages/simple/'

# Send a GET request to the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all country containers
countries = soup.find_all('div', class_='col-md-4 country')

# Initialize a list to hold each country's data
data = []

# Iterate through each country and extract details
for country in countries:
    name = country.find('h3', class_='country-name').get_text(strip=True)
    capital = country.find('span', class_='country-capital').get_text(strip=True)
    population = country.find('span', class_='country-population').get_text(strip=True).replace(',', '')
    area = country.find('span', class_='country-area').get_text(strip=True).replace(',', '')
    
    # Convert numeric strings to proper data types
    try:
        population = int(population)
    except ValueError:
        population = None

    try:
        area = float(area)
    except ValueError:
        area = None

    data.append({
        'Name': name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Optional: sort by population or area if desired
df.sort_values(by='Population', ascending=False, inplace=True)

# Export to CSV
df.to_csv('countries_cleaned.csv', index=False, encoding='utf-8')

print("Data scraped and saved to countries_cleaned.csv")

