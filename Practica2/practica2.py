#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
# Distribución normal
xn = np.random.randn(1, 5)
#%%
#x= range(3000)
y_randn = np.random.randn(3000)
plt.plot(y_randn)
plt.show()
#%%
plt.hist(y_randn, 25)
plt.show()
#%%
y = np.random.randn(30000)
plt.plot(y)
plt.show()
#%%
plt.hist(y, 25)
plt.show()
#%%
# Distribucion uniforme
xu = np.random.rand(1, 5)
#%%
y_randu = np.random.rand(3000)
plt.plot(y_randu)
plt.show()
#%%
plt.hist(y_randu, 25)
plt.show()
#%%
# Ahora con 30,000 muesteas
y = np.random.rand(30000)
plt.plot(y)
plt.show()
#%%
plt.hist(y, 25)
plt.show()
#%%
# Al multiplicar la función por un escalar, le modificamos la desviación estándar
y = 5*y_randn
plt.plot(y)
plt.show()
z = plt.hist(y, 25)

#%%
# Cuando le restamos o sumamos un escalar, le modificamos la media
y  = (5*y_randn-10)
plt.plot(y)
plt.show()
z=plt.hist(y, 25)
#%%
# Modificar varianza a dist. uniforme
y = 5*y_randu
plt.plot(y)
plt.show()
z = plt.hist(y, 25)

#%%
# Cuando le restamos o sumamos un escalar, le modificamos la media
y  = (5*y_randu-10)
plt.plot(y)
plt.show()
z=plt.hist(y)
#%%
# Sumando dos variables con distribución normal
y = y_randn+(5*y_randn-10)
plt.plot(y)
plt.show()
plt.hist(y,25)
#%%
# Ahora sumamos una v.a. con distribución normal con 
# una con distribución uniforme
y = y_randn + y_randu
plt.plot(y)
plt.show()
plt.hist(y, 25)
plt.show()
#%%
# Multiplicamos dos v.a con distribución gaussiana
y = y_randn * y_randn
plt.plot(y)
plt.show()
plt.hist(y, 25)
plt.show()
#%%
# Multiplicamos dos v.a con distribución normail
y = y_randu * y_randu
plt.plot(y)
plt.show()
plt.hist(y, 25)
plt.show()

#%%
# media y desviacion estandar de la distribución normail
media = np.mean(y_randn)
print('Media = ', media)
desv_est = np.std(y_randn)
print('Std = ', desv_est)
var = desv_est**2
print('Varianza = ', var)
#%%
# media y desviacion estandar de la distribución uniforme
media = np.mean(y_randu)
print('Media = ', media)
desv_est = np.std(y_randu)
print('Std = ', desv_est)
var = desv_est**2
print('Varianza = ', var)

#%%
# Generar una distribución conjunta, dos normales
# una con media 0 y desv est de 1 y la otra con media 2 y desv est de 4
conj_x = y_randn
conj_y = 4*y_randn+2