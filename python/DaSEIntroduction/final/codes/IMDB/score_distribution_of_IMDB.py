import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
for encoding in encoding_list:
    try:
        df = pd.read_csv('IMDBTop250.csv', encoding=encoding)
        break
    except UnicodeDecodeError:
        pass

df['rating'] = pd.to_numeric(df['rating'])

df = df.dropna(subset=['rating'])

rating_counts = df['rating'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(rating_counts.index, rating_counts.values, color='orange')
plt.title('IMDBTop250不同评分的电影个数')
plt.xlabel('评分')
plt.ylabel('电影个数')
plt.show()