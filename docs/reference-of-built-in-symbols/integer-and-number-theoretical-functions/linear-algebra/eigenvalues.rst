Eigenvalues
===========

`Matrix Eigenvalues <https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors>`_     (`WMA link <https://reference.wolfram.com/language/ref/Eigenvalues.html>`_)



:code:`Eigenvalues` [:math:`m`]
    computes the eigenvalues of the matrix :math:`m`.
    
    By default, Sympy's routine is used. Sometimes this is slow and       less good than the corresponding mpmath routine.
    
    Use option Method->"mpmath" if you want to use mpmath's routine instead.





Numeric eigenvalues are sorted in order of decreasing absolute value:

>>> Eigenvalues[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}]
  = {2, -1, 1}

Symbolic eigenvalues:

>>> Eigenvalues[{{Cos[theta],Sin[theta],0},{-Sin[theta],Cos[theta],0},{0,0,1}}] // Sort
  = {1, Cos[theta] + Sqrt[(-1 + Cos[theta]) (1 + Cos[theta])], Cos[theta] - Sqrt[(-1 + Cos[theta]) (1 + Cos[theta])]}
>>> Eigenvalues[{{7, 1}, {-4, 3}}]
  = {5, 5}
>>> Eigenvalues[{{7, 1}, {-4, 3}}]
  = {5, 5}
