from bs4 import BeautifulSoup

with open('./page_source.html','r', encoding='utf-8') as html_file:
    source = html_file.read()

    soup = BeautifulSoup(source,'html.parser')
    content = soup.find('ul' , class_ = 'nav nav-list')
    for tags in soup.find_all(True):
        if tags.string:
            print(f"tag: <{tags.name}> Text: {tags.string}")



