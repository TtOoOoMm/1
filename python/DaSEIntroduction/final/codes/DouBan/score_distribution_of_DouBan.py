import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv', encoding='utf-8')

rating_counts = df['评分'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(rating_counts.index, rating_counts.values, color='green')
plt.title('DouBanTop250不同评分的电影个数')
plt.xlabel('评分')
plt.ylabel('电影个数')
plt.show()