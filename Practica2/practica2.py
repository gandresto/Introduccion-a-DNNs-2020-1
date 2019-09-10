#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
# Distribución normal
x = np.random.randn(1, 5)
#%%
#x= range(3000)
y_randn = np.random.randn(1, 3000)
plt.plot(y_randn)
plt.show()
#%%
plt.hist(y_randn, 50)
plt.show()
#%%
y = np.random.randn(1, 30000)
plt.plot(y)
plt.show()
#%%
plt.hist(y, 50)
plt.show()
#%%
# Distribucion uniforme
x = np.random.rand(1, 5)
#%%
y_randu = np.random.rand(1, 3000)
plt.plot(y_randu)
plt.show()
#%%
plt.hist(y_randu, 50)
plt.show()
#%%
# Ahora con 30,000 muesteas
y = np.random.rand(1, 30000)
plt.plot(y)
plt.show()
#%%
plt.hist(y, 50)
plt.show()
#%%
# Al multiplicar la función por un escalar, le modificamos la varianza
y = 5*y_randn
plt.plot(y)
plt.show()
z = plt.hist(y)

#%%
# Cuando le restamos o sumamos un escalar, le modificamos la media
y  = (5*y_randn-10)
plt.plot(y)
plt.show()
z=plt.hist(y)
#%%
# Modificar varianza a dist. uniforme
y = 5*y_randu
plt.plot(y)
plt.show()
z = plt.hist(y)

#%%
# Cuando le restamos o sumamos un escalar, le modificamos la media
y  = (5*y_randu-10)
plt.plot(y)
plt.show()
z=plt.hist(y)
#%%
y = y_randn+(5*y_randn-10)
plt.plot(y)
plt.show()
plt.hist(y)
#%%
# Ahora sumamos una v.a. con distribución normal con 
# una con distribución uniforme
y = y_randn + y_randu
plt.plot(y)
plt.show()
plt.hist(y)
plt.show()
#%%
# Multiplicamos dos v.a con distribución gaussiana
y = y_randn * y_randn
plt.plot(y)
plt.show()
plt.hist(y)
plt.show()
#%%
# Multiplicamos dos v.a con distribución normail
y = y_randu * y_randu
plt.plot(y)
plt.show()
plt.hist(y)
plt.show()

#%%
# media y desviacion estandar de la distribución normail
x = y_randn
media = np.mean(x)
desv_est = np.std(x)
var = desv_est**2
#%%
# media y desviacion estandar de la distribución uniforme
x = y_randu
media = np.mean(x)
desv_est = np.std(x)
var = desv_est**2

# Generar una distribución conjunta, dos normales
# una con media 0 y desv est de 1 y la otra con media 2 y desv est de 4