import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y_exact = np.sin(x)

noise = np.random.normal(0, 0.2, 50)
y_noisy = y_exact + noise

plt.plot(x, y_exact, label='Exact sin(x)')
plt.scatter(x, y_noisy, label='Noisy Data')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exact vs Noisy Sine Wave')
plt.legend()
plt.grid()

plt.show()