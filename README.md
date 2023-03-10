# Multivariate-Analysis
In this repository we can find the theory and the Python code for the multivariate analysis part of the course "Advanced Computational Physics" 
of the Master in Physics of the University of Santiago de Compostela. 

**Note: All these programs are made without using any Python statistics library.**

## Exercise 0. *Regression on a 2D space*

A program that given a set of data $(x_1, y_1), ..., (x_n , y_n)$ read from a file:

1. Evaluates $mean(x)$, $mean(y)$, $\sigma_x$ , $\sigma_y$ , and the correlation
coefficient, $\rho$.
2. Defines two functions $f_y(x)$ and $f_x(y)$ such that given $x$ (respectively $y$) evaluates the best possible choice of $y$
(respectively $x$) compatible with the above data.
3. Plot the data points. Plot the two lines.

In this program we use the data in file **test0.dat** *(You can find this file in the datasets folder)*.

## Exercise 1. *Regression on a k - D space*

A program that given a set of data $(x_{11}, ..., x_{1k}), ..., (x_{n1}, ..., x_{nk})$ read from a file:

1. Evaluates $mean(x_{\alpha})$, $mean(y_{alpha})$, and the correlation matrix.
2. Defines a function such that given a set of indices $\alpha_1, ... \alpha_l,$  $l < k$, and a set of numbers $x_1...x_l$ calculates the best
possible choice for the rest of variables.

In this program we use the data in file **test1.dat** *(You can find this file in the datasets folder)*.

## Exercise 2. *PCA analysis in k dimensions*

A program that given a set of data $(x_{11}, x_{22}, ..., x_{1k}), ..., (x_{n1}, x_{n2} ..., x_{nk})$ read from a file:

1. Evaluates the PCA: Evaluates the eigenvalues, sorts them and choose the two largest eigenvalues.
2. Projects every event onto the subspace of the two eigenvectors.
3. Projects every variable onto the subspace.

In this program we can use data in files:
**test_iris.dat** Data of individual measurement of specimens of the Iris flower.
**test_temperature.dat** Data of the monthly average temperature of several European cities.
**test_santiago.dat** Data of the daily temperature and pressure of Santiago.
*(You can find this file in the datasets folder)*.














