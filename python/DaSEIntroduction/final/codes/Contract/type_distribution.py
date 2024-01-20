import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df_douban = pd.read_csv('DouBanTop250.csv')
df_imdb = pd.read_csv('IMDBTop250.csv')


label_dict = {
    '动作': 'Action',
    '冒险': 'Adventure',
    '动画': 'Animation',
    '传记': 'Biography',
    '喜剧': 'Comedy',
    '犯罪': 'Crime',
    '剧情': 'Drama',
    '家庭': 'Family',
    '奇幻': 'Fantasy',
    '黑色电影': 'Film-Noir',
    '历史': 'History',
    '恐怖': 'Horror',
    '音乐': 'Music',
    '音乐剧': 'Musical',
    '悬疑': 'Mystery',
    '爱情': 'Romance',
    '科幻': 'Sci-Fi',
    '运动': 'Sport',
    '惊悚': 'Thriller',
    '战争': 'War',
    '西部': 'Western'
}

def translate_labels(df, label_dict):
    genres = df['类型'].str.split(' ').sum()
    genre_counts = dict(Counter(genres))
    genre_counts = {k: v for k, v in sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)[:20]}
    genre_counts = {label_dict[k]: v for k, v in genre_counts.items() if k in label_dict}
    return genre_counts

douban_genre_counts = translate_labels(df_douban, label_dict)
imdb_genre_counts = translate_labels(df_imdb, label_dict)

shared_genres = {k: douban_genre_counts[k] for k in douban_genre_counts if k in imdb_genre_counts}
unique_douban_genres = {k: douban_genre_counts[k] for k in douban_genre_counts if k not in imdb_genre_counts}
unique_imdb_genres = {k: imdb_genre_counts[k] for k in imdb_genre_counts if k not in douban_genre_counts}

fig, ax = plt.subplots(figsize=(10, 6))

positions = np.arange(len(shared_genres))

# 绘制共有类型的条形图
ax.barh(positions, list(shared_genres.values()), color='green', height=0.3, label='Shared Genres (豆瓣 & IMDB)')

# 绘制豆瓣独有的类型的条形图
ax.barh(positions + 0.3, list(unique_douban_genres.values()), color='orange', height=0.3, label='豆瓣 Top250 Unique Genres')

# 设置图表的标题、标签等
ax.set_xlabel('数量')
ax.set_ylabel('电影类型')
ax.set_yticks(positions + 0.15)
ax.set_yticklabels(list(shared_genres.keys()))

ax.legend()

# 显示图表
plt.title('类型分布')  # 图表标题
plt.tight_layout()
plt.show()