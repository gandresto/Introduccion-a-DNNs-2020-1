import numpy as np
import perceptron as per

p_vect = [np.matrix([1, -1, -1]), np.matrix([1, 1, -1])]
t_vect = [0, 1]

w = np.matrix([1, -1, -0.5])
b = np.matrix([1])

epochs = 10
e_vect = []

for i in range(epochs):
    for p, t in zip(p_vect, t_vect):
        #print('Para el punto p = ', p)
        a = per.afn(p, w, b)
        #print('a = ', a)
        e = per.efn(t, a)
        e_vect.append(e)
        #print('e = ', e)
        w, b = per.reglaApr(w, b, e, p)
        #print('w = ', w)
        #print('b = ', b)
        print("Epoca %d, Error = %d" % (i, e))