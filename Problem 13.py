import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)   # Must be positive!

y = x**2

plt.subplot(2,1,1)
plt.plot(x, y)
plt.title('Normal Scale')
plt.grid()

plt.subplot(2,1,2)
plt.plot(x, y)
plt.xscale('log')
plt.yscale('log')
plt.title('Log-Log Scale')
plt.grid()

plt.tight_layout()
plt.show()