import pandas as pd
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

plt.figure(figsize=(10, 6))
plt.barh([label_dict[key] for key in genre_counts.keys()], genre_counts.values(), color='blue')
plt.xlabel('电影数量')
plt.ylabel('电影类型')
plt.title('IMDBTop250不同类型电影的分布情况')
plt.show()