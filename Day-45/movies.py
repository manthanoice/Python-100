from re import U
from bs4 import BeautifulSoup
import requests

content = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
movies = content.text

soup = BeautifulSoup(movies, 'html.parser')

#making list so can append later
movie_list = []

#finding the mvoies using beautifulsoup
movies_name = soup.find_all(name='h3', clasS_='jsx-4245974604')
for i in movies_name:
    movie_list.append(i.getText())

print(movie_list)

#Well I guess it's not working idk why, I tred but it doesn't work :P