from bs4 import BeautifulSoup

with open(r'beautifulsoup\page_source.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "html.parser")
    tags = soup.find_all('li' , class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for tag in tags:
        book_name = tag.h3.text
        book_price = tag.p.text
        print(book_name)
        print(book_price)



    