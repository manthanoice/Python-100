import requests
from bs4 import BeautifulSoup

#Making requests and getting the data
response = requests.get(url='https://news.ycombinator.com/')
content = response.text

#making the lists to store the data we scrape
the_titles = []
the_links = []
the_scores = []

#let's make the soup shall we? By the permission of Gordon Ramsay
soup = BeautifulSoup(content, 'html.parser')
the_title = soup.find_all('a', class_='titlelink')
for i in the_title:
    the_titles.append(i.getText())

for i in the_title:
    the_links.append(i.get('href'))

the_score = soup.find_all('span', class_='score')
for i in the_score:
    the_scores.append(int(i.getText().split()[0]))

#Finding the article with maximum upvotes at the current moment and storing that data and printing it! And could send the mail to user using smtp!
max_upvotes = max(the_scores)
max_index = the_scores.index(max_upvotes)
print(the_titles[max_index])
print(the_links[max_index])