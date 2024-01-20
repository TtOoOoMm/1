import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('IMDBTop250.csv')

release_years = df['year'].astype(str).str.extract('(\d{4})')[0].astype(int)

year_counts = release_years.value_counts().sort_index()

plt.bar(year_counts.index, year_counts.values)
plt.xlabel('上映年份')
plt.ylabel('电影数量')
plt.title('IMDBTop250在不同年份的分布情况')
plt.show()