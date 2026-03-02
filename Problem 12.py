import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

plt.subplot(2,1,1)
plt.plot(x, x**2, color='red', label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(x, x**3, color='blue', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^3')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()