import requests
from bs4 import BeautifulSoup

# Skicka en förfrågan till webbsidan
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)

if response.status_code == 200:
    # Analysera HTML-koden med BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Hitta alla boktitlar
    # Boktitlar finns under <h3> taggarna på sidan
    books = soup.find_all('h3')

    # Skriv ut alla titlar
    for book in books:
        title = book.a['title']
        print(title)
else:
    print(f"Fel vid anslutning, statuskod: {response.status_code}")
