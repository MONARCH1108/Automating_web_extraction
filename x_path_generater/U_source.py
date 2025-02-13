from lxml import etree

def get_xpath(element):
    path = []
    while element is not None:
        if element.get("id"):
            path.append(f"//*[@id='{element.get('id')}']")
            break
        
        parent = element.getparent()
        if parent is None:
            break

        siblings = parent.findall(element.tag)
        if len(siblings) == 1:
            path.append(element.tag)
        else:
            index = siblings.index(element) + 1
            path.append(f"{element.tag}[{index}]")
        element = parent

    return '/' + '/'.join(reversed(path))
def get_xpath_by_text(html_content, search_text):
    tree = etree.HTML(html_content)
    elements = tree.xpath(f"//*[contains(text(), '{search_text}')]")
    if not elements:
        return f"No element found containing text: '{search_text}'"

    element = elements[0]
    xpath = get_xpath(element)
    return xpath

with open(r"C:\Users\abhay\OneDrive\Desktop\main_testing\source.html", 'r', encoding='UTF-8') as f:
    html_content = f.read()

search_text = input('Enter string: ')
xpath = get_xpath_by_text(html_content, search_text)
print("XPath:", xpath)
