NullSpace
=========

`Kernel (null space) <https://en.wikipedia.org/wiki/Kernel_(linear_algebra)>`_     (`WMA link <https://reference.wolfram.com/language/ref/NullSpace.html>`_)


:code:`NullSpace` [:math:`matrix`]
    returns a list of vectors that span the nullspace of :math:`matrix`.





>>> NullSpace[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}]

    =
:math:`\left\{\left\{1,-2,1\right\}\right\}`


>>> A = {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}};


>>> NullSpace[A]

    =
:math:`\left\{\right\}`


>>> MatrixRank[A]

    =
:math:`3`


