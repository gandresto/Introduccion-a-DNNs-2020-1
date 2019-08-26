import numpy as np
import matplotlib.pyplot as plt

# 3. 
x = np.random.rand(1000)
y = np.random.randn(1000)

plt.subplot(2, 1, 1)
plt.plot(x)
plt.subplot(2, 1, 2)
plt.plot(y)

plt.show()