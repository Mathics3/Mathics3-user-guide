LucasL
======

`Lucas Number <https://en.wikipedia.org/wiki/Lucas_number>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.numbers.lucas>`_,     `WMA <https://reference.wolfram.com/language/ref/LucasL.html>`_)


:code:`LucasL` [:math:`n`]
    gives the :math:`n`th Lucas number.

:code:`LucasL` [:math:`n`, :math:`x`]
    gives the :math:`n`th Lucas polynomial :math:`L_(x)`.





A list of the first five Lucas numbers:

>>> Table[LucasL[n], {n, 1, 5}]
  = {1, 3, 4, 7, 11}
>>> Series[LucasL[1/2, x], {x, 0, 5}]
  = 1 + 1 / 4 x + 1 / 32 x ^ 2 + (-1 / 128) x ^ 3 + (-5 / 2048) x ^ 4 + 7 / 8192 x ^ 5 + O[x] ^ 6
>>> Plot[LucasL[1/2, x], {x, -5, 5}]
  = -Graphics-
