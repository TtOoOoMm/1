import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
for encoding in encoding_list:
    try:
        df = pd.read_csv('imdb_top250_movies.csv', encoding=encoding)
        break
    except UnicodeDecodeError:
        pass

df['imdbVotes'] = pd.to_numeric(df['imdbVotes'].str.replace(',', ''), errors='coerce')
df['imdbRating'] = pd.to_numeric(df['imdbRating'], errors='coerce')

df = df.dropna(subset=['imdbVotes', 'imdbRating'])
ratings = df['imdbRating']
num_ratings = df['imdbVotes']

S = np.mean(ratings)
V = np.mean(num_ratings)

normalized_ratings = ratings / S
normalized_num_ratings = num_ratings / V

def update_plot(weight1):
    weight2 = 1 - weight1

    weights = [weight1, weight2]
    weighted_sum = weights[0] * normalized_ratings + weights[1] * normalized_num_ratings

    rankings = df['Num']

    plt.scatter(rankings, weighted_sum)
    plt.xlabel('排名')
    plt.ylabel('评价参数')
    plt.title('IMDB排名和评价参数的关系')
    plt.show()

interact(update_plot, weight1=(0, 1, 0.01))