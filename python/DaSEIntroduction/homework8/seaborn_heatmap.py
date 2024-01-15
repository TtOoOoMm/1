import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(data=tips, x="total_bill", y="tip")

plt.title('Regression Plot')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.show()