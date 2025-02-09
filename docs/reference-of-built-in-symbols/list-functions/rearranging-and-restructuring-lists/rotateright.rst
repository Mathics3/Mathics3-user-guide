RotateRight
===========

`WMA link <https://reference.wolfram.com/language/ref/RotateRight.html>`_


:code:`RotateRight` [:math:`expr`]
    rotates the items of :math:`expr`' by one item to the right.

:code:`RotateRight` [:math:`expr`, :math:`n`]
    rotates the items of :math:`expr`' by :math:`n` items to the right.

:code:`RotateRight` [:math:`expr`, {:math:`n_1`, :math:`n_2`, ...}]
    rotates the items of :math:`expr`' by :math:`n_1` items to the right at the first level, by :math:`n_2` items to the right at the second level, and so on.





>>> RotateRight[{1, 2, 3}]

    =
:math:`\left\{3,1,2\right\}`


>>> RotateRight[Range[10], 3]

    =
:math:`\left\{8,9,10,1,2,3,4,5,6,7\right\}`


>>> RotateRight[x[a, b, c], 2]

    =
:math:`x\left[b,c,a\right]`


>>> RotateRight[{{a, b, c}, {d, e, f}, {g, h, i}}, {1, 2}]

    =
:math:`\left\{\left\{h,i,g\right\},\left\{b,c,a\right\},\left\{e,f,d\right\}\right\}`


