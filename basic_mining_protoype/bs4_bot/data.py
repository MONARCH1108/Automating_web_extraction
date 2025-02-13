from bs4 import BeautifulSoup
import requests
import spacy

nlp = spacy.load("en_core_web_sm")
url = input("Enter the URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
only_text = soup.get_text(strip=True)

doc = nlp(only_text)
with open("data.txt", "w", encoding='UTF-8') as f:
    for sent in doc.sents:
        f.write(str(sent) + '\n')

    f.write("\nLinks:\n")
    for link in soup.find_all('a', href=True):
        f.write(f"Link: {link.get('href')}\n")
        f.write(f"Text: {link.get_text(strip=True)}\n\n")
