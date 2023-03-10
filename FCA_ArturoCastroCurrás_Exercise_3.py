# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:30:36 2022

@author: acasc
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('test_cluster.dat').T

M = 5 #Supongo que hay 5 clústers.

K, N = np.shape(data)

#'N' es el número de eventos o puntos.
#'K' es el número de variables.

#defino la funcion que calculará la distancia entre dos puntos r1 y r2 k-dimensionales.
def fdis(r1, r2):
    """
    Parameters
    ----------
    r1 : Tupla o lista con las coordenadas del primer  punto
    r2 : Tupla o lista con las coordenadas del segundo punto.

    Returns
    -------
    La distancia entre los puntos.

    """
    
    dis2 = np.linalg.norm([r1[i] - r2[i] for i in range(len(r1))])
    
    return np.sqrt(dis2)

# Asigno centros x0, y0,... aleatorios a cada clúster:

center = np.zeros((K, M))

#Cada columna son las coordenadas del centro de cada clúster.
#Hay K filas con M columnas.

for i in range(K):
    xmin = np.min(data[i]) #Minimo valor en la coordenada i de los datos.
    xmax = np.max(data[i]) #Maximo valor en la coordenada i de los datos.
    for m in range(M):
        center[i][m] = np.random.rand() * (xmax - xmin) + xmin




#A cada centro le asigno los vectores mas proximos para formar los clústeres:

def fassign_cluster(x, center):
    """
    Parameters
    ----------
    x : Lista con las corrdenadas del punto de interes.
    center : Array con las coordenadas de los centros de los clústeres.

    Returns
    -------
    cluster : El indicativo numerico del clúster al que pertenece el 
                       punto.

    """   
    dis = fdis(x, center[:, 0]) #Distancia del punto al clúster 1.
    cluster = 1 #Se asigna el punto al clúster 1.
    
    for i in range(1, M): #Se comprueba si el punto esta mas cerca del resto de clústers.
                          
        test = fdis(x, center[:, i])
        if test <= dis :
            dis = test
            cluster = i + 1
            
    return cluster
    
#Creo una lista en la que se indique el clúster al que pertenece cada punto asignando cada punto al clúster mas proximo.
cluster = [fassign_cluster(data[:, i], center) for i in range(N)]

         
#Calculo el nuevo centro de gravedad con una función para la siguiente particion:

def fgravity(x, cluster):
    """
    Parameters
    ----------
    x : array con la posicion de todos los puntos.
    cluster : lista con la etiqueta del clúster al que pertenece
                       cada punto.

    Returns
    -------
    center : array con los centros de todos los clústeres, siendo
                      las coordenadas las columnas.

    """
    fil, col = np.shape(x) # fil nº coordenadas, col nºpuntos        
    center = np.zeros((fil, M))    
    aux = M * [0] 
    
    for i in range(col):         
        j = cluster[i] - 1        
        aux[j] = aux[j] + 1         
        center[:, j] = center[:, j] + data[:, i]
  
    for m in range(M): 
        center[:, m] = center[:, m] / aux[m]
    
    return center

#Número de iteraciones antes de la convergencia del algoritmo.
convergencia = 'no'
n = 0 

#escribo el algoritmo
while convergencia == 'no':
    #Lista con los clústeres a los que pertenece cada punto:
    cluster0 = cluster
    
    #Paso 1: calculo los nuevos centros de gravedad de la particion:
    center = fgravity(data, cluster)
    
    #Paso 2: asigno a cada punto un (nuevo) clúster:
    cluster = [fassign_cluster(data[:, i], center) for i in range(N)]
    
    n = n + 1 #Añado 1 al número de iteraciones realizadas.
    
    #Paso 3: comparo si todos los puntos pertenecen al mismo clúster antes de
    #la iteracion actual y despues de ella:
    if np.all(cluster0 == cluster):
        convergencia = 'si'
    
print('El algoritmo ha convergido tras %d iteraciones' %(n))


#Ploteo la distribucion de puntos en las dos primeras coordenadas:

#Asigno a cada clúster un color
col = [(i/M, (M+1-i)/M, (M/3-1)/M) for i in range(1, M+1)]

plt.close('all')
plt.figure()
for i in range(N):
    index = cluster[i]
    plt.plot(data[0,i], data[1,i], 'o', color = col[index-1])

plt.plot(center[0], center[1], 'k*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Agrupacion de los puntos en clusters')
plt.show()