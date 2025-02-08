Dimensions
==========

`WMA <https://reference.wolfram.com/language/ref/Dimensions.html>`_


:code:`Dimensions` [:math:`expr`]
    returns a list of the dimensions of the expression :math:`expr`.





A vector of length 3:

>>> Dimensions[{a, b, c}]
    =

:math:`\left\{3\right\}`



A 3x2 matrix:

>>> Dimensions[{{a, b}, {c, d}, {e, f}}]
    =

:math:`\left\{3,2\right\}`



Ragged arrays are not taken into account:

>>> Dimensions[{{a, b}, {b, c}, {c, d, e}}]
    =

:math:`\left\{3\right\}`



The expression can have any head:

>>> Dimensions[f[f[a, b, c]]]
    =

:math:`\left\{1,3\right\}`


