import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('DouBanTop250.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['排名'], df['评分'], alpha=0.5, color='green')
plt.title('豆瓣Top250电影排名和评分关系')
plt.xlabel('排名')
plt.ylabel('评分')

x = df['排名']
y = df['评分']
fit = np.polyfit(x, y, 3)
fit_fn = np.poly1d(fit)

x_plot = np.linspace(1, 250, 250)
plt.plot(x_plot, fit_fn(x_plot), color='red')

plt.show()