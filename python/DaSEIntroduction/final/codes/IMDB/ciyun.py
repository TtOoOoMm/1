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

label_dict = {
    'Action': '动作',
    'Adventure': '冒险',
    'Animation': '动画',
    'Biography': '传记',
    'Comedy': '喜剧',
    'Crime': '犯罪',
    'Drama': '剧情',
    'Family': '家庭',
    'Fantasy': '奇幻',
    'Film-Noir': '黑色电影',
    'History': '历史',
    'Horror': '恐怖',
    'Music': '音乐',
    'Musical': '音乐剧',
    'Mystery': '悬疑',
    'Romance': '爱情',
    'Sci-Fi': '科幻',
    'Sport': '运动',
    'Thriller': '惊悚',
    'War': '战争',
    'Western': '西部'
}

words = []
for types in df['genre']:
    for word in types.split(','):
        if word.strip() in label_dict:
            words.append(label_dict[word.strip()])
        else:
            words.append(word.strip())

seg_list = jieba.cut(','.join(words), cut_all=False)
seg_list = ','.join(seg_list).split()

font_path = 'simhei.ttf'

wordcloud = WordCloud(
    background_color='white',
    font_path=font_path,
    max_words=20,
    min_font_size=10,
    max_font_size=100,
).generate(",".join(seg_list))

plt.imshow(wordcloud)
plt.axis('off')
plt.title('IMDB不同电影类型的词云')
plt.show()