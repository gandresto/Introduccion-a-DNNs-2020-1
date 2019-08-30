# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:01:38 2019

@author: Andres
"""
#%%
import numpy as np

#%%
# 2.
A=np.array([[1,3,-2],
            [4,5,0],
            [-1,2,4]])

#%%
print('Transpuesta de A')
np.transpose(A)

#%%
print('Inversa de A')
np.invert(A)

#%%
print('Determinante de A')
np.linalg.det(A)

#%%
print('Traza de A')
np.trace(A)

#%%
print('Valores propios de A')
np.linalg.eigvals(A)

#%%
print('Vecotres propios de A')
np.linalg.eig(A)

#%%
print('Resolver sistema de ecuaciones de forma Ax=b')
b=np.array([[1],
            [3],
            [0]])
np.linalg.solve(A, b)