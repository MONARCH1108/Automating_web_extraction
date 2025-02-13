from bs4 import BeautifulSoup
import requests

response = requests.get('https://books.toscrape.com/index.html')
soup = BeautifulSoup(response.text, 'lxml')
with open('source.html','w',encoding='UTF-8') as f:
    f.write(soup.prettify())