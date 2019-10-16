import numpy as np

def h(x, theta0=0, theta1=1):
    return theta0 + x*theta1

def fc_min_cuadrados(xvect = [], yvect=[], theta0=0, theta1=1):
    J = 0
    m = len(xvect)
    for x, y in zip(xvect, yvect):
        J += (h(x, theta0, theta1)-y)**2
        print(J)
    J /= (2*m)
    print('')
    return J

datax = [2,2,6,7]
datay = [1,3,6,9]

costo_a = fc_min_cuadrados(datax, datay, 0, 2)
costo_b = fc_min_cuadrados(datax, datay, 2, 1)
costo_c = fc_min_cuadrados(datax, datay, -1, 3)

print(costo_a, costo_b, costo_c)