import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

encoding_list = ['utf-8', 'ISO-8859-1', 'utf-16']
success = False
for encoding in encoding_list:
    try:
        df = pd.read_csv('imdb_top250_movies.csv', encoding=encoding)
        success = True
        break
    except UnicodeDecodeError:
        pass

if not success:
    raise Exception("Failed to read the CSV file with all attempted encodings")

df['imdbVotes'] = pd.to_numeric(df['imdbVotes'].str.replace(',', ''), errors='coerce')
df['Num'] = pd.to_numeric(df['Num'], errors='coerce')

df = df.dropna(subset=['imdbVotes', 'Num'])

plt.figure(figsize=(10, 6))
plt.scatter(df['Num'], df['imdbVotes'], alpha=0.5)
plt.title('IMDBTop250电影排名和评价人数关系')
plt.xlabel('排名')
plt.ylabel('评价人数')
plt.show()