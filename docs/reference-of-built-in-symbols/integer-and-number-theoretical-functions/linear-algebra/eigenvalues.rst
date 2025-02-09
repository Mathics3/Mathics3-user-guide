Eigenvalues
===========

`Matrix Eigenvalues <https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors>`_     (`WMA link <https://reference.wolfram.com/language/ref/Eigenvalues.html>`_)



:code:`Eigenvalues` [:math:`m`]
    computes the eigenvalues of the matrix :math:`m`.
    
    By default, Sympy's routine is used. Sometimes this is slow and       less good than the corresponding mpmath routine.
    
    Use option Method->"mpmath" if you want to use mpmath's routine instead.





Numeric eigenvalues are sorted in order of decreasing absolute value:

>>> Eigenvalues[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}]

    =
:math:`\left\{2,-1,1\right\}`



Symbolic eigenvalues:

>>> Eigenvalues[{{Cos[theta],Sin[theta],0},{-Sin[theta],Cos[theta],0},{0,0,1}}] // Sort

    =
:math:`\left\{1,\text{Cos}\left[\text{theta}\right]+\sqrt{\left(-1+\text{Cos}\left[\text{theta}\right]\right) \left(1+\text{Cos}\left[\text{theta}\right]\right)},\text{Cos}\left[\text{theta}\right]-\sqrt{\left(-1+\text{Cos}\left[\text{theta}\right]\right) \left(1+\text{Cos}\left[\text{theta}\right]\right)}\right\}`


>>> Eigenvalues[{{7, 1}, {-4, 3}}]

    =
:math:`\left\{5,5\right\}`


>>> Eigenvalues[{{7, 1}, {-4, 3}}]

    =
:math:`\left\{5,5\right\}`


