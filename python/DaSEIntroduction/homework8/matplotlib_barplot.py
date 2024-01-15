import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

plt.bar(categories, values)

plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()