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

1. Evaluates $mean(x_{\alpha})$, $mean(y_{\alpha})$, and the correlation matrix.
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

## Exercise 3. *Cluster analysis*

A program which makes an analysis of clusters using the k-means algorithm. Given a set of k-dimensional data, we write a program to calculate
the best choice for $M$ clusters using the k-means algorithm *(Lloyd’s algorithm)*. Given a set of data $\vec{x_i}, ..., \vec{x_N}$ where each vector $\vec{x_i}$ belongs to a k-dimensional space, we will look for the existence of clusters of data, i.e.: We will try to determine whether the data
can be splitted into $s$ classes, $S_{\alpha}$, such that for every event we can say that $\vec{x_i} \in S_{\alpha}$ for some $\alpha = 1,...,s$.

Assuming that the number of clusters is known, $M$. The problem consists on finding the centers of the $M$ clusters such that the sum of the distances of every point to its cluster is minimized. **The LLoyd’s algorithm can be implemented like this:**

1. Start with a initial arbitrary partition $P_0$ (for instance choose random centers $z_1, ..., z_M$ for the $M$ clusters).
2. In step $n$, evaluate the “gravity center”, $g_n(q)$ for each cluster $q$ of the partition $P_n$.
3. Reassign each event to the nearest cluster (using the distance to the gravity center). This produces a new partition $P_{n+1}$.
4. If the new partition is different from the previous one go to step 1. If it is the same, the algorithm has converged.

The algorithm may not converge to the optimal clustering. One way to avoid this is to start with several initial partitions $P_0$ and choose the best one.

In this program we use the data from file **test_cluster.dat**, but you can use the same data as in the previus program *(Exercise 2)*. We use the hyperparamether $M = 5$ to test for this data. *(You can find this file in the datasets folder)*.



## Exercise 4. *Agglomerate Hierarchical Clustering*

A program which make an analysis of clusters by using the *Ward’s algorithm*. Given a set of k-dimensional data, we write a program to calculate a hierarchical tree of clusters. The algorithm of Ward’s is a classical algorithm which is useful for small number of events. It starts by building the distance between every pair of events. **The LLoyd’s algorithm can be implemented like this:**

1. Define $d(i, l)$ the distance between events $\vec{x_i}$ and $\vec{x_l}$.
2. Find the pair of events $(i, l)$ with the smallest $d(i, l)$.
3. Group together the events $\vec{x_i}$ and $\vec{x_l}$ , and produce a “grouped event” or agglomerate $\vec{x_{il}}$.
4. From the matrix $d$, delete the rows and columns $i$ and $l$.
5. Add a new row and column $il$ by evaluating the distance from every other event to the new agglomerate.
6. Repeat step 1, until all the events are grouped together and only survives one single group.

The data are the same as in the previous program.







