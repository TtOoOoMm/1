import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

df = pd.read_csv('imdb.csv')

country_mapping = {
    'United States': '美国',
    'United Kingdom': '英国',
    'Germany': '德国',
    'Canada': '加拿大',
    'France': '法国',
    'Japan': '日本',
    'Italy': '意大利',
    'Australia': '澳大利亚',
    'India': '印度',
    'Spain': '西班牙',
}

country_counts = {}
for countries in df['country']:
    if isinstance(countries, str):
        countries = countries.split(',')
        for country in countries:
            country = country.strip()
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

top_countries = sorted(country_counts, key=country_counts.get, reverse=True)[:10]

translated_countries = [country_mapping.get(country, country) for country in top_countries]

labels = translated_countries
values = [country_counts[country] for country in top_countries]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('IMDBTop250电影第一制作国家占比')
plt.show()