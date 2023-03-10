# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:43:30 2022

@author: acasc
"""
import numpy as np

#Cargo los datos del problema
datos = np.loadtxt('test1.dat')
F,C = datos.shape

#Separo las variable x1, x2, ... xN
x = []
for i in range(C):
    x.append(datos.T[i])
x = np.array(x)

#defino la media 
def mean(x):
    mean = np.sum(x)/len(x)
    return mean

#defino la varianza
def sigma(x):
    m = mean(x)
    m2 = mean(x*x)
    sigma = np.sqrt(m2-m*m)
    return sigma

#defino la funcion para la matriz correlación
def rho(x,y):
    mx = mean(x)
    my = mean(y)
    elemxy =np.sum( (x-mx)*(y-my))/len(x)
    return elemxy

#defino la funcion estimacon
def f_estimacion(a,xa,x,V):
    """
    Parameters
    ----------
    a : indices conocidos.
    xa : valor de las variables conocidas.
    x : datos del problema.
    V : inversa de la matriz de correlacion.

    Returns
    -------
    b : indices desconocidos.
    y : mejor estimacion de los valores de las variables a conocer.
    
    """
    b = [i for i in range(C) if i not in a]
    delta = [(xa[i]-mean(x[a[i]])) for i in range(len(xa))]
    V_ba = np.array(V[np.ix_(b,a)])
    V_bb = np.array(V[np.ix_(b,b)])
    rho_bb = np.array(np.linalg.inv(V_bb))
    K = rho_bb.dot(V_ba).dot(delta)
    y = [mean(x[b[i]]) - K[i] for i in range(len(K))]
    return b, y

#calculo la matriz de correlacion
M = np.zeros((C,C))
for i in range(C):
    for j in range(C):
        M[i][j] = rho(x[i],x[j])

#obtengo la inversa de la matriz de correlacion y meto los indices
#y los valores de las variables de prueba
V = np.linalg.inv(M)
a = np.array([0,1,2])
xa = np.array([5,2,23])

#aplico la funcion
y = f_estimacion(a,xa,x,V)

#muestro los resultados por terminal
print(y)
