#%%
from gradesc import gradesc

#%%
theta = 1
lr = 0.1
iterac = 2
x=[1,2,3]
y=[2,4,5.8]

#%%
theta = gradesc(x, y, theta, lr, iterac)

#%%
