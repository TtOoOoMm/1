import pandas as pd

df_douban = pd.read_csv('DouBanTop250.csv', encoding='utf-8')

mean_douban = df_douban['评分'].mean()

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
for encoding in encoding_list:
    try:
        df_imdb = pd.read_csv('IMDBTop250.csv', encoding=encoding)
        break
    except UnicodeDecodeError:
        pass

mean_imdb = df_imdb['rating'].mean()

print('豆瓣 Top250 的均分：', mean_douban)
print('IMDb Top250 的均分：', mean_imdb)