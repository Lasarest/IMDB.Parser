from bs4 import BeautifulSoup
import requests
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(url)
filteredFilms = []
allFilms = []
allRating = []
soup = BeautifulSoup(page.text, "html.parser")
allFilms = soup.findAll('td', class_='titleColumn')
for data in allFilms:
    if data.find('a') is not None:
        filteredFilms.append(data.text)
allFilms.clear()
for data in filteredFilms:
    filtered = data[16:]
    data = filtered[:-8]
    allFilms.append(data)
filteredFilms.clear()
allRating = soup.findAll('td', class_='ratingColumn imdbRating')
for data in allRating:
    if data.find('strong') is not None:
        filteredFilms.append(data.text)
allRating.clear()
for data in filteredFilms:
    filtered = data[1:4]
    allRating.append(filtered)
Result_Dictionary = dict(zip(allFilms,allRating))
print(Result_Dictionary)