import numpy as np

def hardlim(x):
    return 1 if x>=0 else 0

def afn(x, w, b):
    return hardlim(w*x.T+b)

def efn(t, a):
    return t-a

def reglaApr(w_ant, b_ant, e, p):
    w_nuevo = w_ant + e*p
    b_nuevo = b_ant + e
    return w_nuevo, b_nuevo