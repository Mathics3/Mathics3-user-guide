Reverse
=======

`WMA link <https://reference.wolfram.com/language/ref/Reverse.html>`_


:code:`Reverse` [:math:`expr`]
    reverses the order of :math:`expr`'s items (on the top level)

:code:`Reverse` [:math:`expr`, :math:`n`]
    reverses the order of items in :math:`expr` on level :math:`n`

:code:`Reverse` [:math:`expr`, {:math:`n_1`, :math:`n_2`, ...}]
    reverses the order of items in :math:`expr` on levels :math:`n_1`, :math:`n_2`, ...





>>> Reverse[{1, 2, 3}]
    =

:math:`\left\{3,2,1\right\}`


>>> Reverse[x[a, b, c]]
    =

:math:`x\left[c,b,a\right]`


>>> Reverse[{{1, 2}, {3, 4}}, 1]
    =

:math:`\left\{\left\{3,4\right\},\left\{1,2\right\}\right\}`


>>> Reverse[{{1, 2}, {3, 4}}, 2]
    =

:math:`\left\{\left\{2,1\right\},\left\{4,3\right\}\right\}`


>>> Reverse[{{1, 2}, {3, 4}}, {1, 2}]
    =

:math:`\left\{\left\{4,3\right\},\left\{2,1\right\}\right\}`


