import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(12, 8))

df = pd.read_csv('DouBanTop250.csv')

plt.scatter(df['排名'], df['评分'], alpha=0.5, color='green', label='豆瓣Top250')

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
for encoding in encoding_list:
    try:
        df = pd.read_csv('imdb_top250_movies.csv', encoding=encoding)
        break
    except UnicodeDecodeError:
        pass

df['imdbRating'] = pd.to_numeric(df['imdbRating'])
df['Num'] = pd.to_numeric(df['Num'], errors='coerce')

df = df.dropna(subset=['imdbRating', 'Num'])

plt.scatter(df['Num'], df['imdbRating'], alpha=0.5, color='orange', label='IMDB Top250')

plt.title('豆瓣Top250与IMDB Top250电影排名和评分关系')
plt.xlabel('排名')
plt.ylabel('评分')
plt.legend()
plt.show()