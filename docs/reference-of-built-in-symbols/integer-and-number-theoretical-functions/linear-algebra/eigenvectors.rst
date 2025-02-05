Eigenvectors
============

`Matrix Eigenvalues <https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors>`_     (`WMA link <https://reference.wolfram.com/language/ref/Eigenvectors.html>`_)


:code:`Eigenvectors` [:math:`m`]
    computes the eigenvectors of the matrix :math:`m`.





>>> Eigenvectors[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}]
  = {{1, 1, 1}, {1, -2, 1}, {-1, 0, 1}}
>>> Eigenvectors[{{1, 0, 0}, {0, 1, 0}, {0, 0, 0}}]
  = {{0, 1, 0}, {1, 0, 0}, {0, 0, 1}}
>>> Eigenvectors[{{2, 0, 0}, {0, -1, 0}, {0, 0, 0}}]
  = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
>>> Eigenvectors[{{0.1, 0.2}, {0.8, 0.5}}]
  = ...
