import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv')

release_years = df['上映年份'].str.extract('(\d{4})')[0].astype(int)

decade_counts = ((release_years // 10) * 10).value_counts().sort_index()

plt.bar(decade_counts.index, decade_counts.values, width=5)
plt.xticks(ticks=decade_counts.index, labels=[str(i)+'s' for i in decade_counts.index], rotation=45)
plt.xlabel('年代（每十年为一个数据点）')
plt.ylabel('电影数量')
plt.title('不同年代豆瓣Top250电影数量的柱状图')
plt.show()