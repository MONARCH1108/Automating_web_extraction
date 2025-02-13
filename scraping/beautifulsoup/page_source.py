from bs4 import BeautifulSoup
import requests

response = requests.get('https://finance.yahoo.com/')
soup = BeautifulSoup(response.text , 'lxml' )
print(soup.prettify())

#above code block for getting the page source in the terminal.
#for printing that entire page in the in an HTML file.

with open('page_source.html', 'w' , encoding= 'utf - 8') as file:
    file.write(soup.prettify())
    

