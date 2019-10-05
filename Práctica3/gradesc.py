import numpy as np

def h(x, theta=1):
    return x*theta

def fc_min_cuadrados(xvect = [], yvect=[], theta=1):
    J = 0
    for x, y in zip(xvect, yvect):
        J = (h(x, theta)-y)**2
    J /= 2*len(xvect)
    return J

def der_min_cuadrados(xvect = [], yvect=[], theta=1):
    J = 0
    for x, y in zip(xvect, yvect):
        J += (h(x, theta)-y)*x
    J /= len(xvect)
    return J

def gradesc(xvect=[], yvect=[], theta=1, lr=0.1, iterac=1):
    for i in range(iterac):
        theta -= lr*der_min_cuadrados(xvect, yvect, theta)
    return theta

