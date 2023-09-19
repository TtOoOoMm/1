import random
import math
import matplotlib.pyplot as plt

mu = 0
sigma = math.sqrt(9)
n1 = 10
n2 = 30
conf_level = 0.95  
n_simulations = 100 

def calc_ci(xbar, s, n):
    alpha = 1 - conf_level
    if n < 30:
        t = 2.048
        margin = t * s / math.sqrt(n)
    else:
        z = 1.96
        margin = z * sigma / math.sqrt(n)
    return (xbar - margin, xbar + margin)

cis1 = []
for i in range(n_simulations):
    xs = [random.gauss(mu, sigma) for j in range(n1)]
    xbar = sum(xs) / n1
    ci = calc_ci(xbar, sigma, n1)
    cis1.append(ci)
    
cis2 = []
for i in range(n_simulations):
    xs = [random.gauss(mu, sigma) for j in range(n2)]
    xbar = sum(xs) / n2
    ci = calc_ci(xbar, sigma, n2)
    cis2.append(ci)
    
cis3 = []
for i in range(n_simulations):
    xs = [random.gauss(mu, sigma) for j in range(n1)]
    xbar = sum(xs) / n1
    s = math.sqrt(sum((x - xbar)**2 for x in xs) / (n1 - 1))
    ci = calc_ci(xbar, s, n1)
    cis3.append(ci)
    
cis4 = []
for i in range(n_simulations):
    xs = [random.gauss(mu, sigma) for j in range(n2)]
    xbar = sum(xs) / n2
    s = math.sqrt(sum((x - xbar)**2 for x in xs) / (n2 - 1))
    ci = calc_ci(xbar, s, n2)
    cis4.append(ci)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

def plot_ci(ax, cis, title):
    ax.plot([0, 100], [mu, mu], 'k--', label='True Mean')
    for i, ci in enumerate(cis):
        ax.plot([i, i], ci, 'b-', linewidth=0.5)
    ax.set_title(title)
    ax.legend()

plot_ci(axs[0][0], cis1, 'case 1')
plot_ci(axs[0][1], cis2, 'case 2')
plot_ci(axs[1][0], cis3, 'case 3')
plot_ci(axs[1][1], cis4, 'case 4')

plt.tight_layout()
plt.show()