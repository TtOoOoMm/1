import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv')

first_country = df['制作国家'].str.split(' ').str[0]

country_counts = first_country.value_counts()

top_10_countries = country_counts.head(10)

plt.pie(top_10_countries.values, labels=top_10_countries.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('豆瓣Top250电影第一制作国家占比')
plt.show()