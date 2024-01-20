import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df_douban = pd.read_csv('DouBanTop250.csv', encoding='utf-8')

rating_counts_douban = df_douban['评分'].value_counts().sort_index()

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
for encoding in encoding_list:
    try:
        df_imdb = pd.read_csv('IMDBTop250.csv', encoding=encoding)
        break
    except UnicodeDecodeError:
        pass

df_imdb['rating'] = pd.to_numeric(df_imdb['rating'])
df_imdb = df_imdb.dropna(subset=['rating'])

rating_counts_imdb = df_imdb['rating'].value_counts().sort_index()

all_ratings = sorted(set(list(rating_counts_douban.index) + list(rating_counts_imdb.index)))

douban_values = [rating_counts_douban.get(rating, 0) for rating in all_ratings]
imdb_values = [rating_counts_imdb.get(rating, 0) for rating in all_ratings]

fig, ax = plt.subplots()
bar_width = 0.4
index = np.arange(len(all_ratings))

bar1 = ax.bar(index, douban_values, bar_width, label='豆瓣电影', color='green')
bar2 = ax.bar(index + bar_width, imdb_values, bar_width, label='IMDb电影', color='orange')

ax.set_xlabel('评分')
ax.set_ylabel('电影个数')
ax.set_title('豆瓣Top250和IMDbTop250不同评分的电影个数')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(all_ratings)
ax.legend()

plt.show()