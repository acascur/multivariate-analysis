# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:39:31 2021

@author: arturo.castro0
"""

import numpy as np

""" Cargamos los datos y eliminamos la columna de eventos"""

x = np.loadtxt('train_fisher_A.dat')
y = np.loadtxt('train_fisher_B.dat')

x_data = np.delete(x, 0, axis=1) #x = x[:,1:col]
y_data = np.delete(y, 0, axis=1) #y = y[:,1:col]

fil, col = np.shape(x_data)

test_A = np.loadtxt('test_fisher_A.dat')
test_B = np.loadtxt('test_fisher_B.dat')

test_A = np.loadtxt('test_fisher_A.dat')
test_B = np.loadtxt('test_fisher_B.dat')

test_A = np.delete(test_A, 0, axis=1) #test_A = test_A[:,1:col]
test_B = np.delete(test_B, 0, axis=1)


""" Defino funciones que me calculen la media, la desviacion y la matriz de correlacion M"""

def f_estadistica(x,y):
    """
    Función que toma los dos array de datos y devuelve la media, desviación
    y matriz de correlacion de los datos.

    Parameters
    ----------
    x : array con los datos x.
    y : array con los datos y.

    Returns
    -------
    
    media, desviación y matriz correlación de los datos.

    """
    media = lambda x: sum(x)/len(x) #calcula la media
    sigma = lambda x: np.sqrt(media(x*x)-media(x**2)) #calcula la desviacion
    correlacion = lambda xi, xj: np.sum((xi-media(xi))*(xj-media(xj)))/len(xi) #calcula la correlacion
    
      
    x_media = media(x); x_sigma = sigma(x) #media de tados x
    y_media = media(y); y_sigma = sigma(y) #media de datos y
    
    Mx = np.array([[correlacion(x[:,i],x[:,j]) for i in range(col)] for j in range(col)]) #matriz 
    My = np.array([[correlacion(y[:,i],y[:,j]) for i in range(col)] for j in range(col)])
    
    return x_media, y_media, x_sigma, y_sigma, Mx, My

x_media, y_media, x_sigma, y_sigma, Mx, My = f_estadistica(x_data, y_data)

""" Calculamos w, F0 y F1 """

w = np.linalg.inv(Mx+My) @ (x_media - y_media)
F0 = w @ x_media
F1 = w @ y_media

""" Clasificamos los eventos en s=0 o s=1. Hacemos el corte en el valor medio de F0 y F1 """

def f_fisher(z):
    """
    

    Parameters
    ----------
    z : TYPE
        DESCRIPTION.

    Returns
    -------
    clase.

    """
    F = w @ z.T
    clase = np.zeros(len(F))
    
    for i in range(len(F)):
        
        if F0 == min(F0, F1):
            if F[i] <= (F0 + F1) * 0.5:
                clase[i] = 0
            else:
                clase[i] = 1 
                
        if F0 == max(F0, F1):
            if F[i] <= (F0 + F1) * 0.5:
                clase[i] = 1
            else: 
                clase[i]
                
    return clase

    
A_clas = f_fisher(test_A)
B_clas = f_fisher(test_B)

A0_sum = sum([+1 for i in A_clas if i == 0])
B0_sum = sum([+1 for i in B_clas if i == 0])

A1_sum = sum([+1 for i in A_clas if i == 1])
B1_sum = sum([+1 for i in B_clas if i == 1])

print('\nPoblación A: ')
print('\nHay %.f elementos de tipo 0 y %.f elementos de tipo 1' % (A0_sum, A1_sum))

print('\nPoblación B: ')
print('\nHay %.f elementos de tipo 0 y %.f elementos de tipo 1' % (B0_sum, B1_sum))



































    