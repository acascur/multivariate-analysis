# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:36:54 2022

@author: acasc
"""

import numpy as np
import matplotlib.pyplot as plt

#Cargo los datos del problema
data = np.loadtxt('test0.dat').T #otra forma sería ---> xdata, ydata = np.loadtxt('test0.dat')

#defino la media y calculo las medias de x e y
media = lambda x: sum(x)/len(x)
mediax = media(data[0]) #otra forma sería ---> mediax = media(xdata)
mediay= media(data[1])

#defino la varianza y calculo para x e y
sigma = lambda x: np.sqrt(media(x*x)-media(x)**2) 
sigmax = sigma(data[0]) #otra forma sería ---> sigmax = sigma(xdata)
sigmay = sigma(data[1])

#calculo el coeficiente de correlacion
ro = (media(data[0]*data[1])-mediax*mediay)/(sigmax*sigmay) #---> ro = (media(xdata*ydata)-mediax*mediay)/(sigmax*sigmay)

#calculo la recta de valores más probables de x e y
xf = lambda y: mediax + ro*sigmax/sigmay*(y-mediay)
yf = lambda x: mediay + ro*sigmay/sigmax*(x-mediax)


#ploteo la gráfica
plt.figure()
plt.scatter(data[0], data[1], c='b', alpha=0.1) #---> plt.scatter(xdata, ydata, c='b', alpha=0.1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Representación gráfica de la regresión en 2D')
plt.plot(data[0],yf(data[0]), c='r') #---> plt.plot(xdata,yf(xdata), c='r')
plt.plot(xf(data[1]), data[1], c='g') #---> plt.plot(xf(ydata), ydata, c='g')
plt.show()

print('\nla media de x es: %.5f y su varianza es: %.5f' % (mediax, sigmax)) 
print('\nla media de y es: %.5f y su varianza es: %.5f' % (mediay, sigmay))
print('\nEl coeficiente de correlación es:', ro)