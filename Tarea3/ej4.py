import numpy as np
import matplotlib.pyplot as plt

def h(x, theta=1):
    return x*theta

def fc_min_cuadrados(xvect = [], yvect=[], theta=1):
    J = 0
    for x, y in zip(xvect, yvect):
        J += (h(x, theta)-y)**2
    J /= 2*len(xvect)
    return J

X = [1,2,3]
Y = [2,4,5.8]
J = []
TH = np.arange(1.8,2.2,0.2)

for theta in TH:
    J.append(fc_min_cuadrados(X,Y,theta))

plt.xlabel("Theta")
plt.ylabel("Costo")
plt.plot(TH, J)
plt.show()