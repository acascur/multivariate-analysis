# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:06:12 2022

@author: acasc
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#cargo datos
data = np.loadtxt('test_cluster.dat',max_rows = 50).T
N = len(data[0]) #Numero de puntos o eventos.

#creo las lista de indices, histogramas y aglomerados que voy a necesitar y donde almaceno los resultados
index = N * [0]
hist = np.copy(data)
histindex = N * [0]
histpunt = [ ] 

#funcion que calcula la distancia euclidea como en el ejercicio de clusters
def fdis(r1, r2):
    """
    Parameters
    ----------
    r1 : Tupla o lista con las coordenadas del primer  punto.
    r2 : Tupla o lista con las coordenadas del segundo punto.

    Returns
    -------
    La distancia entre los puntos.

    """
    
    dis2 = np.linalg.norm([r1[i] - r2[i] for i in range(len(r1))])
    
    return np.sqrt(dis2)

#Creo un array con las distancias entre los eventos xi y xl:
d = np.zeros((N,N))
for i in range(N):
    for j in range(i+1, N):
        aux = fdis(data[:, i], data[:, j])
        d[i][j] = aux
        d[j][i] = aux

dismax = np.max(d) #Distancia maxima entre eventos.

#creo una funcion que devulve indices de dos puntos más cercanos
def fdismin(d):
    """
    Parameters
    ----------
    d : Matriz con las distancias entre eventos.

    Returns
    -------
    i : El indice del primer  evento.
    l : El indice del segundo evento.

    """
    fil, col = np.shape(d)   
    dis = dismax
    
    i = 0
    l = 0    
    for j in range(0, fil):
        for k in range(j+1,col):
            if d[j][k] < dis:
                
                i = j
                l = k
                dis = d[j][k]
    return i, l

#funcion que calcula coordenadas de un aglomerado de 2 eventos ponderando.
def fagglomerate(i, l, data, index):
    """
    Parameters
    ----------
    i : El indice del primer  evento.
    l : El indice del segundo evento.
    data : El array de puntos.
    index : Lista de indicativos de los puntos.

    Returns
    -------
    pos : Las coordenadas del nuevo aglomerado.
    newindex : El indicativo del nuevo aglomerado.

    """
    w1 = index[i] + 1
    w2 = index[l] + 1
    
    pos = w1*data[:, i] + w2*data[:, l]
    pos = [i / (w1 + w2) for i in pos]
    
    #Calculo el indicativo mayor de los dos puntos.
    oldindex = max(index[i], index[l]) 
    #El indicativo del aglomerado sera el mayor de los dos originales mas 1:
    newindex = oldindex + 1
    
    return (pos, newindex) 

    

#funcion que elimina de las matrices d, data, index las filas y columnas correspondientes a i y l
def fdelete(d, data, index, i, l):
    """
    Parameters
    ----------
    d : Array de distancias.
    data : El array de puntos.
    index : Lista de indicativos de los puntos.
    i : indice del primer evento para eliminar.
    l : indide del segundo evento para eliminar.

    Returns
    -------
    d : array de distancias sin las filas y columnas 'i' y 'l'.
    data : array de puntos con las columnas 'i' y 'l' eliminadas.
    index : Lista de indicativos de los puntos con las posiciones 'i'
                     y 'l' eliminadas.

    """
    
    d = np.delete(d, (i, l), axis = 0)
    d = np.delete(d, (i, l), axis = 1)
    
    data  = np.delete(data, (i, l), axis = 1)
    index = list(np.delete(index, (i, l)))
    
    return (d, data, index)

#Ahora añade a lo anterior el nuevo aglomerado
def finsert(d, data, index, xil, newindex):
    """
    Parameters
    ----------
    d : Array de distancias.
    data : Array de puntos.
    index : Lista de indicativos de los puntos.
    xil : Lista con las coordenadas (x, y) del nuevo aglomerado.
    newindex : Indicativo del nuevo aglomerado.

    Returns
    -------
    d : arrray de distancias con la fila y columna del nuevo aglomerado.
    data : array de puntos con el nuevo aglomerado.
    index : lista de indicativos con el indicativo del nuevo aglomerado.

    """
    
    #Añado el aglomerado a data:
    data  = np.concatenate((data, np.array([xil]).T), axis = 1) 
    #Añado a la lista de indicativos el indicativo del nuevo aglomerado:
    index.append(newindex) 
    
    fil, col = np.shape(d)
    
    newcol = np.zeros((fil, 1))    #Creo la nueva columna con distancias.
    newfil = np.zeros((1, col +1)) #Creo la nueva   fila  con distancias.
    
    #Calculo las distancias del aglomerado al resto de puntos:
    for i in range(fil):
        newcol[i,0] = fdis(data[:, i], xil)
        newfil[0,i] = newcol[i, 0]
    
    d = np.concatenate((d, newcol), axis = 1)   #Añado la columna al array d.
    d = np.concatenate((d, newfil),   axis = 0) #Añado la   fila  al array d.
   
    return d, data, index


#graficamos las posiciones de los eventos y la creacion de aglomerados.
plt.close('all')
fig, ax1 = plt.subplots()
fig, ax2 = plt.subplots()

ax1.plot(data[0], data[1], 'o', markersize = 1)
ax1.set_xlabel('Posicion x del evento')
ax1.set_ylabel('Posicion y del evento')
ax1.set_title('Proceso de creacion de aglomerados')

ax2.plot(data[0], N*[0], 'o')
ax2.set_xlabel('Posicion x del evento')
ax2.set_ylabel('Orden gerarquico')
ax2.set_title('Organizacion de los eventos en categorias.')
indexplot = 1
col = cm.jet(0.0)

#akgoritmo por pasos para graficar
while(len(data[0])) > 1:
    #(1) busco la minima distancia entre dos puntos
    i, l = fdismin(d)
    
    p1 = data[:, i]
    p2 = data[:, l]
    
    for k in range(len(hist[0])):
        if (hist[:, k] == p1).all() :
            t1 = k
        if (hist[:, k] == p2).all() :
            t2 = k
    
    histpunt.append((t1, t2))
    
    #(2)agrupo los eventos 'i', 'l' en un aglomerado con la media
    xil, newindex = fagglomerate(i, l, data, index)
    
    #graficando los nuevos aglomerados:   
    if newindex != indexplot:
        col = cm.jet (newindex/(np.sqrt(2*N)))
        indexplot = newindex
        
    ax1.plot(xil[0], xil[1], 'o', markersize = newindex, color = col)
    ax1.plot([data[0, i], xil[0]], [data[1, i], xil[1]], '--', color = col)
    ax1.plot([data[0, l], xil[0]], [data[1, l], xil[1]], '--', color = col)

    ax2.plot(xil[0], newindex, 'o', color = col)
    ax2.vlines(data[0, i], ymin=index[i], ymax=newindex, color = col)
    ax2.vlines(data[0, l], ymin=index[l], ymax=newindex, color = col)
    xmi =  min(data[0, i], data[0, l], xil[0])
    xma =  max(data[0, i], data[0, l], xil[0])
    ax2.hlines(newindex, xmin = xmi, xmax = xma, color = col)
    
    #(3) de la matriz 'd' elimino las filas y columnas 'i' y 'l'
    d, data, index = fdelete(d, data, index, i, l)

    #(4) añado una nueva fila y una nueva columna evaluando la d desde el resto de puntos al aglomerado
    d, data, index = finsert(d, data, index, xil, newindex)

    #Añado al historial el ultimo aglomerado
    hist = np.concatenate((hist, np.array([data[:, -1]]).T), axis = 1)
    #Añado a la lista de indicativos del historial el indicativo del ultimo aglomerado
    histindex.append(index[-1])
    
    
#tengo el array hist, con todos los eventos y aglomerados almacenados en columnas.
    
#tengo la lista histindex, que me dice si una columna en 'hist' corresponde a un evento, aglomerado de 1ºorden, de 2º...
    
#tengo la lista histpunt que contiene tuplas (i, l) de cada aglomerado, puntos con los que se forman.


plt.show()
print('Los eventos se agrupan en %d niveles.' %(np.max(histindex)\
                                                            + 1))