from bs4 import BeautifulSoup
from git import head

with open(r'E:\Python 100\Day-45\website.html', encoding='utf8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.string)

all_para = soup.find_all(name='a')
for text in all_para:
    print(text.get('href'))

class_is_heading = soup.find_all(class_ = 'heading')
print(class_is_heading)

name = soup.select_one('#name')
for i in name:
    print(i.getText())

headings = soup.select('.heading')
for i in headings:
    print(i.getText())