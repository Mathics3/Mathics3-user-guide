Linear algebra
==============

Let's consider the matrix

>>> A = {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}};


>>> MatrixForm[A]
    =

:math:`\left(\begin{array}{ccc} 1 & 1 & 0\\ 1 & 0 & 1\\ 0 & 1 & 1\end{array}\right)`



We can compute its eigenvalues and eigenvectors:

>>> Eigenvalues[A]
    =

:math:`\left\{2,-1,1\right\}`


>>> Eigenvectors[A]
    =

:math:`\left\{\left\{1,1,1\right\},\left\{1,-2,1\right\},\left\{-1,0,1\right\}\right\}`



This yields the diagonalization of :code:`A` :

>>> T = Transpose[Eigenvectors[A]]; MatrixForm[T]
    =

:math:`\left(\begin{array}{ccc} 1 & 1 & -1\\ 1 & -2 & 0\\ 1 & 1 & 1\end{array}\right)`


>>> Inverse[T] . A . T // MatrixForm
    =

:math:`\left(\begin{array}{ccc} 2 & 0 & 0\\ 0 & -1 & 0\\ 0 & 0 & 1\end{array}\right)`


>>> % == DiagonalMatrix[Eigenvalues[A]]
    =

:math:`\text{True}`



We can solve linear systems:

>>> LinearSolve[A, {1, 2, 3}]
    =

:math:`\left\{0,1,2\right\}`


>>> A . %
    =

:math:`\left\{1,2,3\right\}`



In this case, the solution is unique:

>>> NullSpace[A]
    =

:math:`\left\{\right\}`



Let's consider a singular matrix:

>>> B = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};


>>> MatrixRank[B]
    =

:math:`2`


>>> s = LinearSolve[B, {1, 2, 3}]
    =

:math:`\left\{-\frac{1}{3},\frac{2}{3},0\right\}`


>>> NullSpace[B]
    =

:math:`\left\{\left\{1,-2,1\right\}\right\}`


>>> B . (RandomInteger[100] * %[[1]] + s)
    =

:math:`\left\{1,2,3\right\}`


