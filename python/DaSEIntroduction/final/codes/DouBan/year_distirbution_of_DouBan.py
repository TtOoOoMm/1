import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv')

release_years = df['上映年份'].str.extract('(\d{4})')[0].astype(int)

year_counts = release_years.value_counts().sort_index()

plt.bar(year_counts.index, year_counts.values)
plt.xlabel('上映年份')
plt.ylabel('电影数量')
plt.title('豆瓣Top250在不同年份的分布情况')
plt.show()