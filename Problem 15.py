import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=40, density=True, alpha=0.6)

plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Normal Distribution')
plt.grid()

plt.show()