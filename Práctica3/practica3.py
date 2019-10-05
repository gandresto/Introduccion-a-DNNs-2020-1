#!/usr/bin/env python
# coding: utf-8

# # Práctica 3. Método del Gradiente Descendente
# 
# Función hipótesis: h(x)=theta\*x
# 
# Función de costo: error mínimo cuadrado

# In[1]:


from gradesc import gradesc, fc_min_cuadrados
import matplotlib.pyplot as plt


# In[2]:


# Valores de entrenamiento
x=[1,2,3]
y=[2,4,5.8]


# In[3]:


# Parámetros iniciales
theta = 1
lr = 0.1
iterac = 3


# In[4]:


theta = gradesc(x, y, theta, lr, iterac)
print('Theta despúes de %i iteraciones: %.4f' % (iterac, theta))
error = fc_min_cuadrados(x, y, theta)
print('Error despúes de %i iteraciones: %.4f' % (iterac, error))


# ## Parar el entrenamiento
# Paramos el entrenamiento cuando el los valores de theta no cambien

# In[5]:


hist_theta = []
hist_error = []
theta = 1
temp = 1000
cond_paro = 0.0001
i = 0
while abs(temp-theta)>cond_paro:
    i+=1
    temp = theta
    theta = gradesc(x, y, theta, lr)
    print('Theta despúes de %i iteraciones: %.4f' % (i, theta))
    error = fc_min_cuadrados(x, y, theta)
    print('Error despúes de %i iteraciones: %.4f' % (i, error))
    
    hist_theta.append(theta)
    hist_error.append(error)


# In[6]:


plt.title('Valor de theta a través de las iteraciones')
plt.plot(hist_theta)


# In[7]:


plt.title('Error a través de las iteraciones')
plt.plot(hist_error)