import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['排名'], df['评价人数'], alpha=0.5)
plt.title('豆瓣Top250电影排名和评价人数关系')
plt.xlabel('排名')
plt.ylabel('评价人数')
plt.show()