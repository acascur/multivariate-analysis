# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:11:33 2021

@author: acasc
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sc


def f_data(x):
    """
    Parameters
    ----------
    x : --> archivo con los datos del problema.

    Returns
    -------
    x_data : --> datos a tratar estadisticamente.
    F: --> nºfilas de los datos.
    C: --> nºcolumnas de los datos.
    
    """
    data = np.genfromtxt(x)
    data = data[:,1:13]
    F, C = data.shape
    x_data = [data[:,i] for i in range(C)]
    
    return x_data, F, C

def f_estadistica(x):
    """
    Parameters
    ----------
    x : --> Es el array con los datos a tratar estadisticamente.

    Returns
    -------
    y: --> El array de los datos normalizados.
    M: --> La matriz de correlación.

    """
    def media(x):
        """ Calcula la media de los datos
        """
        return np.sum(x)/float(len(x))
            
    def sigma(x):
        """ Calcula la desviación estadística de los datos
        """
        return np.sqrt(media(x*x)-media(x)**2)
            
    def correlacion(x, y):
        """ Obtiene la matriz de correlación
        """
        return np.sum((x-media(x))*(y-media(y))/float(len(x)))
        
    y = np.array([(x[i]-media(x[i]))/sigma(x[i]) for i in range(len(x))])
        
    M = np.array([[correlacion(y[i],y[j]) for i in range(len(x))] for j in range(len(x))])
        
    return y, M

def f_eigenmatrix(M, y):
    """
    Parameters
    ----------
    M : --> matriz de correlacion..

    Returns
    -------
    v1 : autovector 1.
    v2 : autovector 2.
    U1 : vector U1.
    U2 : vector U2.

    """
    eigenval, eigenvec = sc.eig(M)
    autoval = np.real(eigenval)
    autovec = [eigenvec[:,i] for i in range(len(x_data))]
    
    #busco el indice maximo del autovalor y su correspondiente autovector
    i1 = np.argmax(autoval)
    #elimino el indice mayor para encontra el segundo mayor
    autoval2 = np.copy(autoval)
    autoval2[i1] = 0
    i2 = np.argmax(autoval2)
    #asigno los autovectores con su correspondoioiente autovalor
    v1 = autovec[i1]
    v2 = autovec[i2]
    
    U1 = v1 @ y
    U2 = v2 @ y
    
    return v1, v2, U1, U2

x_data, F, C = f_data('test_temperature.dat') #cargo los datos
y, M = f_estadistica(x_data) #los trato estadísticamente
v1, v2, U1, U2 = f_eigenmatrix(M, y) #obtengo los vectores U1 y U2

plt.plot(U1, U2, 'bo') #ploteo todo
plt.xlabel('$U_1$', fontsize=13); plt.ylabel('$U_2$', fontsize=13, rotation = 0)
plt.tight_layout()
plt.show()


#Proyección de cada variable en el subespacio de autovectores:
varx = F * [0]
vary = F * [0]

for i in range(C):
    varx[i] = v1[i]
    vary[i] = v2[i]
    
#Dibujo los resultados: 
plt.figure()
plt.hlines(0, -1, 1, colors = 'blue', linestyles = '--') #Eje x
plt.vlines(0, -1, 1, colors = 'blue', linestyles = '--') #Eje y
x = np.linspace(-1, 1, 300) #Circunferencia
plt.plot(x , np.sqrt(1 - x*x), color = 'lightblue') #Circunferencia
plt.plot(x, -np.sqrt(1 - x*x), color = 'lightblue') #Circunferencia

for i in range(C):
    plt.plot([0, varx[i]], [0, vary[i]], color = 'black')
plt.xlabel('Coordenada 1')
plt.ylabel('Coordenada 2')
plt.show()






    





    
    
