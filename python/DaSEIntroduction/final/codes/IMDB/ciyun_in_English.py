import pandas as pd
import numpy as np
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('IMDBTop250.csv')

genres = df['genre'].str.split(',').sum()

genre_counts = dict(Counter(genres))

genre_counts = {k: v for k, v in sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)[:20]}

words = []
for types in df['genre']:
    for word in types.split():
        if len(word) > 1:
            words.append(word)
        else:
            words.append(types)

seg_list = jieba.cut(' '.join(words))

wordcloud = WordCloud(
    background_color='white',
    font_path='msyh.ttc',
    max_words=20,
    min_font_size=10,
    max_font_size=100,
).generate(" ".join(genre_counts))

plt.imshow(wordcloud)
plt.axis('off')
plt.title('IMDB不同电影类型的词云')
plt.show()