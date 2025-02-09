Binomial
========

`Binomial Coefficient <https://en.wikipedia.org/wiki/Binomial_coefficient>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#binomial>`_, `WMA <https://reference.wolfram.com/language/ref/Binomial.html>`_)


:code:`Binomial` [:math:`n`, :math:`k`]
    gives the binomial coefficient :math:`n` choose :math:`k`.





>>> Binomial[5, 3]

    =
:math:`10`



:code:`Binomial`  supports inexact numbers:

>>> Binomial[10.5,3.2]

    =
:math:`165.286`



Some special cases:

>>> Binomial[10, -2]

    =
:math:`0`


>>> Binomial[-10.5, -3.5]

    =
:math:`0.`


