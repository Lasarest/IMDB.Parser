# Importing packages bs4 and requests, input url
from bs4 import BeautifulSoup
import requests
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(url)
filteredFilms = []
allFilms = []
allRating = []
# Getting code from page
soup = BeautifulSoup(page.text, "html.parser")
allFilms = soup.findAll('td', class_='titleColumn')
# Getting text from tag "a"
for data in allFilms:
    if data.find('a') is not None:
        filteredFilms.append(data.text)
allFilms.clear()
for data in filteredFilms:
    filtered = data[16:]
    data = filtered[:-8]
    allFilms.append(data)
filteredFilms.clear()
# Getting film rating from tag "tb"
allRating = soup.findAll('td', class_='ratingColumn imdbRating')
for data in allRating:
    if data.find('strong') is not None:
        filteredFilms.append(data.text)
allRating.clear()
for data in filteredFilms:
    filtered = data[1:4]
    allRating.append(filtered)
# Joining two dictionaries
Result_Dictionary = dict(zip(allFilms,allRating))
print(Result_Dictionary)
