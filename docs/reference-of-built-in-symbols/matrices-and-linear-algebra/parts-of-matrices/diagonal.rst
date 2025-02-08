Diagonal
========

`WMA link <https://reference.wolfram.com/language/ref/Diagonal.html>`_


:code:`Diagonal` [:math:`m`]
    gives a list with the values in the diagonal of the matrix :math:`m`.

:code:`Diagonal` [:math:`m`, :math:`k`]
    gives a list with the values in the :math:`k` diagonal of the             matrix :math:`m`.





>>> Diagonal[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}]
    =

:math:`\left\{1,5,9\right\}`



Get the superdiagonal:

>>> Diagonal[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 1]
    =

:math:`\left\{2,6\right\}`



Get the subdiagonal:

>>> Diagonal[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, -1]
    =

:math:`\left\{4,8\right\}`



Get the diagonal of a nonsquare matrix:

>>> Diagonal[{{1, 2, 3}, {4, 5, 6}}]
    =

:math:`\left\{1,5\right\}`


