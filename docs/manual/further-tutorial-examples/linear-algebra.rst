Linear algebra
==============

Let's consider the matrix

>>> A = {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}};

>>> MatrixForm[A]
  = 1   1   0
    
    1   0   1
    
    0   1   1

We can compute its eigenvalues and eigenvectors:

>>> Eigenvalues[A]
  = {2, -1, 1}
>>> Eigenvectors[A]
  = {{1, 1, 1}, {1, -2, 1}, {-1, 0, 1}}

This yields the diagonalization of :code:`A` :

>>> T = Transpose[Eigenvectors[A]]; MatrixForm[T]
  = 1   1    -1
    
    1   -2   0
    
    1   1    1
>>> Inverse[T] . A . T // MatrixForm
  = 2   0    0
    
    0   -1   0
    
    0   0    1
>>> % == DiagonalMatrix[Eigenvalues[A]]
  = True

We can solve linear systems:

>>> LinearSolve[A, {1, 2, 3}]
  = {0, 1, 2}
>>> A . %
  = {1, 2, 3}

In this case, the solution is unique:

>>> NullSpace[A]
  = {}

Let's consider a singular matrix:

>>> B = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

>>> MatrixRank[B]
  = 2
>>> s = LinearSolve[B, {1, 2, 3}]
  = {-1 / 3, 2 / 3, 0}
>>> NullSpace[B]
  = {{1, -2, 1}}
>>> B . (RandomInteger[100] * %[[1]] + s)
  = {1, 2, 3}
