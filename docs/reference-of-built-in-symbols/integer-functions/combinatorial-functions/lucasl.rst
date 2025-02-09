LucasL
======

`Lucas Number <https://en.wikipedia.org/wiki/Lucas_number>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.numbers.lucas>`_,     `WMA <https://reference.wolfram.com/language/ref/LucasL.html>`_)


:code:`LucasL` [:math:`n`]
    gives the :math:`n`th Lucas number.

:code:`LucasL` [:math:`n`, :math:`x`]
    gives the :math:`n`th Lucas polynomial :math:`L_(x)`.





A list of the first five Lucas numbers:

>>> Table[LucasL[n], {n, 1, 5}]

    =
:math:`\left\{1,3,4,7,11\right\}`


>>> Series[LucasL[1/2, x], {x, 0, 5}]

    =
:math:`1+\frac{1}{4} x+\frac{1}{32} x^2+\left(-\frac{1}{128}\right) x^3+\left(-\frac{5}{2048}\right) x^4+\frac{7}{8192} x^5+O\left[x\right]^6`


>>> Plot[LucasL[1/2, x], {x, -5, 5}]

    =
.. image:: tmp64a_8rrb.png
    :align: center



