from tempfile import SpooledTemporaryFile
from bs4 import BeautifulSoup
import requests

date = input('Enter which date you wanna time travel to in format YYYY-MM-DD: ')

response = requests.get(url='https://www.billboard.com/charts/hot-100/{}/'.format(date))
content = response.text

soup = BeautifulSoup(content, 'html.parser')

song_list = []
artist_list = []

#Getting the top song
first_song = soup.find('h3', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')
song_list.append(first_song.getText().strip())

#Getting the rest 99 songs
song_names = soup.find_all('h3', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
for i in song_names:
    song_list.append(i.getText().strip())

#Getting top artist
first_artist = soup.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
artist_list.append(first_artist.getText().strip())

#Getting 99 artists
artist_names = soup.find_all('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
for i in artist_names:
    artist_list.append(i.getText().strip())

print(song_list)
print(artist_list)