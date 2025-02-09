Drop
====

`WMA link <https://reference.wolfram.com/language/ref/Drop.html>`_


:code:`Drop` [:math:`list`, :math:`n`]
    returns :math:`list` with the first :math:`n` elements removed.

:code:`Drop` [:math:`list`, -:math:`n`]
    returns :math:`list` with its last :math:`n` elements removed.

:code:`Drop` [:math:`list`, {:math:`m`, :math:`n`}]
    returns :math:`list` with elements :math:`m` though :math:`n` removed.





Drop up until the third item from the beginning of a list:

>>> Drop[{a, b, c, d}, 3]

    =
:math:`\left\{d\right\}`



Drop until the second item from the end of that list:

>>> Drop[{a, b, c, d}, -2]

    =
:math:`\left\{a,b\right\}`



Drop from the second item to the second-to-the-end item:

>>> Drop[{a, b, c, d, e}, {2, -2}]

    =
:math:`\left\{a,e\right\}`



Drop a submatrix:

>>> A = Table[i*10 + j, {i, 4}, {j, 4}]

    =
:math:`\left\{\left\{11,12,13,14\right\},\left\{21,22,23,24\right\},\left\{31,32,33,34\right\},\left\{41,42,43,44\right\}\right\}`


>>> Drop[A, {2, 3}, {2, 3}]

    =
:math:`\left\{\left\{11,14\right\},\left\{41,44\right\}\right\}`



Dropping the 0th element does nothing, and returns the list unmodified:

>>> Drop[{a, b, c, d}, 0]

    =
:math:`\left\{a,b,c,d\right\}`



Even if the list is empty:

>>> Drop[{}, 0]

    =
:math:`\left\{\right\}`



See also `:code:`Take`  </doc/reference-of-built-in-symbols/list-functions/elements-of-lists/take/>`_.