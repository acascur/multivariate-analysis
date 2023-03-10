# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:34:22 2022

@author: acasc
"""
import numpy as np
import neurolab as nl

#Datos para entrenar la red:
datA = np.loadtxt('train_fisher_A.dat')
datB = np.loadtxt('train_fisher_B.dat')
datA = np.delete(datA, 0, axis = 1)
datB = np.delete(datB, 0, axis = 1)
fil, col = np.shape(datA)

#Datos para probar la red:
testA = np.loadtxt('test_fisher_A.dat')
testB = np.loadtxt('test_fisher_B.dat')
testA = np.delete(testA, 0, axis = 1)
testB = np.delete(testB, 0, axis = 1)
 

#Creo una red 'feedforward' con una capa de entrada, una capa oculta y una capa de salida

#La lista con las neuronas escogidas en las capas que no son de entrada es:
neuronas = [3, 1] #3 neuronas en la capa oculta, 1 neurona en la de salida.

#Habra tantos inputs como coordenadas de los eventos:
inputs = col

#Para saber el rango de los inputs:
lim = col * [0]
for i in range(col):
    lim[i] = [min(np.min(datA[:, i]), np.min(datB[:, i])), \
              max(np.max(datA[:, i]), np.max(datB[:, i]))]

#Creo una red con dos capas de 3 y 1 neurona, mas la de entrada: 
red = nl.net.newff(lim, neuronas)
red.init()

#Hay que entrenar a la red. Utilizo el metodo 'backpropagation'. La salida de las entradas de la poblacion 1 sera 0 y la de la poblacion 2 sera 1. 
entrada = np.concatenate((datA, datB), axis = 0)
salida  = np.array([len(datA) * [0] + len(datB) * [1]]).T

#comando en internet
train = red.train(entrada, salida, epochs = 200, show = 10, goal = 0.02)

#epochs : numero de ciclos de entrenamiento.
#show : cada cuantos ciclos se hace un print
#goal : diferencia entre el error en un ciclo y el anterior buscada.

#Para crear la matriz de confusion, introduzco como input los eventos con los que se ha entrenado a la red.
AA = red.sim(datA)
BB = red.sim(datB)

#Como la salida de los eventos de la calse A es 0 y la de los eventos de clase B es 1, distingo entre clases tomando como valor de corte 0.5:

A0 = sum([1 for i in range(len(AA)) if AA[i] <= 0.5])
A1 = sum([1 for i in range(len(AA)) if AA[i] >= 0.5])

B0 = sum([1 for i in range(len(BB)) if BB[i] <= 0.5])
B1 = sum([1 for i in range(len(BB)) if BB[i] >= 0.5])

conf = np.array([[A0, B0],[A1, B1]])

print('\n La matriz de confusion obtenida con los eventos con los que se \
entrena la red neuronal es:')
print(conf)

print('\nHay %d elementos de la poblacion A clasificados correctamente como de\
 la poblacion A' %(A0))
    
print('\nHay %d elementos de la poblacion A clasificados erroneamente como de\
 la poblacion B' %(A1))
    
print('\nHay %d elementos de la poblacion B clasificados correctamente como de\
 la poblacion B' %(B1))
    
print('\nHay %d elementos de la poblacion A clasificados erroneamente como de\
 la poblacion B' %(B0))
    
#Aplico la red

AA = red.sim(testA)
BB = red.sim(testB)

A0 = sum([1 for i in range(len(AA)) if AA[i] <= 0.5])
A1 = sum([1 for i in range(len(AA)) if AA[i] >= 0.5])

B0 = sum([1 for i in range(len(BB)) if BB[i] <= 0.5])
B1 = sum([1 for i in range(len(BB)) if BB[i] >= 0.5])

conf = np.array([[A0, B0],[A1, B1]])

print('\nEn el archivo test_fisher_A.dat hay %d elementos de la poblacion A y \
%d elementos de la poblacion B.' %(A0, A1))
        
print('\nEn el archivo test_fisher_B.dat hay %d elementos de la poblacion A y \
%d elementos de la poblacion B.' %(B0, B1))

print('\nEn este caso la matriz de confusion seria:')
print(conf)


#si me falla vuelvo a ejecutar hasta que funcione.
if A0 == len(datA) and A1 == 0 and B0 == len(datB) and B1 == 0:
    print('\nHa ocurrido un error en el entrenamiento de la red. \n\
Ejecutar el programa de nuevo por favor.')
if A1 == len(datA) and A0 == 0 and B1 == len(datB) and B0 == 0:
    print('\nHa ocurrido un error en el entrenamiento de la red. \n\
Ejecutar el progama de nuevo por favor.')