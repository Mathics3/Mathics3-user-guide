RotateLeft
==========

`WMA link <https://reference.wolfram.com/language/ref/RotateLeft.html>`_


:code:`RotateLeft` [:math:`expr`]
    rotates the items of :math:`expr`' by one item to the left.

:code:`RotateLeft` [:math:`expr`, :math:`n`]
    rotates the items of :math:`expr`' by :math:`n` items to the left.

:code:`RotateLeft` [:math:`expr`, {:math:`n_1`, :math:`n_2`, ...}]
    rotates the items of :math:`expr`' by :math:`n_1` items to the left at           the first level, by :math:`n_2` items to the left at the second level, and so on.





>>> RotateLeft[{1, 2, 3}]
    =

:math:`\left\{2,3,1\right\}`


>>> RotateLeft[Range[10], 3]
    =

:math:`\left\{4,5,6,7,8,9,10,1,2,3\right\}`


>>> RotateLeft[x[a, b, c], 2]
    =

:math:`x\left[c,a,b\right]`


>>> RotateLeft[{{a, b, c}, {d, e, f}, {g, h, i}}, {1, 2}]
    =

:math:`\left\{\left\{f,d,e\right\},\left\{i,g,h\right\},\left\{c,a,b\right\}\right\}`


