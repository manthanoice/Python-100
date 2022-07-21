from bs4 import BeautifulSoup
import requests

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

respose = requests.get(url='https://www.imdb.com/chart/top/', headers=header).text

soup = BeautifulSoup(respose, 'html.parser')

all_elements = soup.select('.titleColumn a')

ratings = soup.select('table.chart td.ratingColumn.imdbRating strong')

all_ratings = []

for i in ratings:
    all_ratings.append(i.getText())

num = 1

the_index = 0

for i in all_elements:
    movies = i.getText()
    print('{}: {}: {}'.format(num, movies, all_ratings[the_index]))
    num+=1
    the_index+=1