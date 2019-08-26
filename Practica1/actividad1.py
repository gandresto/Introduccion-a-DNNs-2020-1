import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, 3, 8, -10])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Vector basura')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
ax.annotate('Subida', xy=(0.75, 1.5),
                        xytext=(0.25, 2),
                        arrowprops={'facecolor' : 'green'})
ax.annotate('Bajada', xy=(2.5, -2.5),
                        xytext=(2, -2),
                        arrowprops={'facecolor' : 'red'})
plt.plot(x, markerfacecolor='blue', marker='o')

plt.show()