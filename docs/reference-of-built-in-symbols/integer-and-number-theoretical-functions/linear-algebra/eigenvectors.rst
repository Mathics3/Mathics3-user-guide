Eigenvectors
============

`Matrix Eigenvalues <https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors>`_     (`WMA link <https://reference.wolfram.com/language/ref/Eigenvectors.html>`_)


:code:`Eigenvectors` [:math:`m`]
    computes the eigenvectors of the matrix :math:`m`.





>>> Eigenvectors[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}]

    =
:math:`\left\{\left\{1,1,1\right\},\left\{1,-2,1\right\},\left\{-1,0,1\right\}\right\}`


>>> Eigenvectors[{{1, 0, 0}, {0, 1, 0}, {0, 0, 0}}]

    =
:math:`\left\{\left\{0,1,0\right\},\left\{1,0,0\right\},\left\{0,0,1\right\}\right\}`


>>> Eigenvectors[{{2, 0, 0}, {0, -1, 0}, {0, 0, 0}}]

    =
:math:`\left\{\left\{1,0,0\right\},\left\{0,1,0\right\},\left\{0,0,1\right\}\right\}`


>>> Eigenvectors[{{0.1, 0.2}, {0.8, 0.5}}]

    =
:math:`\left\{\left\{-0.355518,-1.15048\right\},\left\{-0.62896,0.777438\right\}\right\}`


