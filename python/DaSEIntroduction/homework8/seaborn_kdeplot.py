import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(data=tips, x="total_bill", hue="time", fill=True, common_norm=False, alpha=.5)

plt.title('Kernel Density Estimate Plot')
plt.xlabel('Total Bill')
plt.ylabel('Density')

plt.show()