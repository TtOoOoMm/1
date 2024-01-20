import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv')

genres = df['类型'].str.split(' ').sum()
genre_counts = dict(Counter(genres))

genre_counts = {k: v for k, v in sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)[:20]}

plt.figure(figsize=(10, 6))
plt.barh(list(genre_counts.keys()), list(genre_counts.values()), color='blue')
plt.xlabel('个数')
plt.ylabel('电影类型')
plt.title('豆瓣Top250不同类型电影的分布情况')
plt.show()