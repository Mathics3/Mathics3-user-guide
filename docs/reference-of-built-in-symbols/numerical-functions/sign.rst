Sign
====

`Sign <https://en.wikipedia.org/wiki/Sign_function>`_ (`WMA link <https://reference.wolfram.com/language/ref/Sign.html>`_)


:code:`Sign` [:math:`x`]
    return -1, 0, or 1 depending on whether :math:`x` is negative, zero, or positive.





>>> Sign[19]
    =

:math:`1`


>>> Sign[-6]
    =

:math:`-1`


>>> Sign[0]
    =

:math:`0`


>>> Sign[{-5, -10, 15, 20, 0}]
    =

:math:`\left\{-1,-1,1,1,0\right\}`



For a complex number, :code:`Sign`  returns the phase of the number:

>>> Sign[3 - 4*I]
    =

:math:`\frac{3}{5}-\frac{4 I}{5}`


