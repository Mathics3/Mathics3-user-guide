Integers
========

`WMA link <https://reference.wolfram.com/language/ref/Integers.html>`_


:code:`Integers`
    the domain of integer numbers, as in :math:`x` in Integers.





Limit a solution to integer numbers:

>>> Solve[-4 - 4 x + x^4 + x^5 == 0, x, Integers]

    =
:math:`\left\{\left\{x->-1\right\}\right\}`


>>> Solve[x^4 == 4, x, Integers]

    =
:math:`\left\{\right\}`


