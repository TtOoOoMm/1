import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

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

plt.figure(figsize=(10, 6))
plt.scatter(df['Num'], df['imdbRating'], alpha=0.5, color='orange')
plt.title('IMDBTop250电影排名和评分关系')
plt.xlabel('排名')
plt.ylabel('评分')


x = df['Num']
y = df['imdbRating']
fit = np.polyfit(x, y, 3)
fit_fn = np.poly1d(fit)

x_plot = np.linspace(1, 250, 250)
plt.plot(x_plot, fit_fn(x_plot), color='red')

plt.show()