import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Law_%26_Order:_Special_Victims_Unit_episodes_(seasons_1%E2%80%9319)"

# Send a GET request to the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <td> elements with the class 'summary'
titles = []
for td in soup.find_all('td', class_='summary'):
    title = td.get_text(strip=True)
    if title:  # Check if the title is not empty
        titles.append(title)

# Print the unique titles
unique_titles = list(set(titles))  # Remove duplicates
for title in unique_titles:
    print(title)
