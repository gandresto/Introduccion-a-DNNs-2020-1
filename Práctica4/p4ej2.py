import numpy as np
import perceptron as per
import matplotlib.pyplot as plt

p_vect = [[1,1], [1,0], [1,2], [5,1], [0,-1], [-1,0], [-2,-1], [-3,-2]]
p_vect = [np.matrix(p) for p in p_vect]
t_vect = [0,0,0,0,1,1,1,1]

w = np.matrix(np.random.rand(2))
b = np.matrix(np.random.rand(1))

lr = 0.5
epochs = 3
e_vect = []

for epoch in range(epochs):
    for i, p in enumerate(p_vect):
        # print('Para el punto p = ', p)
        a = per.afn(p, w, b)
        # print('a = ', a)
        e = per.efn(t_vect[i], a)
        e_vect.append(e)
        # print('e = ', e)
        w, b = per.reglaApr(w, b, e, p, lr)
        # print('w = ', w)
        # print('b = ', b)
        if i % 4 == 0:
            print("Epoca %d (%i/%i), Error = %d" % (epoch, i, len(p_vect), e))

plt.plot(e_vect)
plt.title('Error vs iteraciones')
plt.ylabel('Error')
plt.xlabel('Iteraciones')
plt.show()