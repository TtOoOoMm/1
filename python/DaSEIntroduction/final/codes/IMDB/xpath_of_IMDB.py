import requests
from lxml import etree
import pandas as pd

df = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'}
columns = ["Rank", "Title", "Year", "Genre", "Rating", "Director", "Cast", "Votes"]

def get_data(html):
    xp = etree.HTML(html)
    rows = xp.xpath('//tbody[@class="lister-list"]/tr')
    for row in rows:
        """Rank、Title、Year、Genre、Rating、Director、Cast、Votes"""
        rank = row.xpath('.//td[@class="posterColumn"]/span[@class="secondaryInfo"]/text()')[0]
        title = row.xpath('.//td[@class="titleColumn"]/a/text()')[0]
        year = row.xpath('.//td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()')[0][1:-1]
        genre = row.xpath('.//td[@class="titleColumn"]/span[@class="genre"]/text()')[0][1:]
        rating = row.xpath('.//td[@class="ratingColumn imdbRating"]/strong/text()')[0]
        director, cast = row.xpath('.//td[@class="titleColumn"]/a/@title')[0][:-1], row.xpath('.//td[@class="titleColumn"]/a/@title')[1:]
        votes = row.xpath('.//td[@class="sort_column"]/span[@name="nv"]/@data-value')[0]
        df.append([rank, title, year, genre, rating, director, cast, votes])
    
    d = pd.DataFrame(df, columns=columns)
    d.to_csv('IMDbTop250.csv', index=False)

for i in range(1, 251, 50):
    url = "https://www.imdb.com/chart/top/?sort=ir,desc&start={}&ref_=adv_nxt".format(i)
    res = requests.get(url, headers=headers)
    html = res.text
    get_data(html)