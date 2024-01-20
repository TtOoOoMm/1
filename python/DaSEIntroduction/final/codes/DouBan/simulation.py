import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('DouBanTop250.csv', encoding='utf-8')
ratings = df['评分']
num_ratings = df['评价人数']

S = np.mean(ratings)
V = np.mean(num_ratings)

normalized_ratings = ratings / S
normalized_num_ratings = num_ratings / V

def update_plot(weight1):
    weight2 = 1 - weight1

    weights = [weight1, weight2]
    weighted_sum = weights[0] * normalized_ratings + weights[1] * normalized_num_ratings

    rankings = df['排名']

    plt.scatter(rankings, weighted_sum)
    plt.xlabel('排名')
    plt.ylabel('评价参数')
    plt.title('豆瓣排名和评价参数的关系')
    plt.show()

interact(update_plot, weight1=(0, 1, 0.01))