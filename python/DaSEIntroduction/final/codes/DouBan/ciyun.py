import pandas as pd
import numpy as np
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('DouBanTop250.csv')

genres = df['类型'].str.split(' ').sum()
genre_counts = dict(Counter(genres))

genre_counts = {k: v for k, v in sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)[:20]}


seg_list = jieba.cut(' '.join(genre_counts))
wordcloud = WordCloud(
    background_color='white',
    font_path='msyh.ttc',
    max_words=20,
    min_font_size=10,
    max_font_size=100,
).generate(" ".join(genre_counts))

plt.imshow(wordcloud)
plt.axis('off')
plt.title('豆瓣不同电影类型的词云')
plt.show()