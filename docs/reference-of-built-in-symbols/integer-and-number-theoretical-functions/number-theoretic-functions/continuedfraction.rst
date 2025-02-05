ContinuedFraction
=================

`Continued fraction <https://en.wikipedia.org/wiki/Continued_fraction>`_ (`SymPy <https://docs.sympy.org/latest/modules/ntheory.html#module-sympy.ntheory.continued_fraction>`_, `WMA <https://reference.wolfram.com/language/ref/ContinuedFraction.html>`_)

:code:`ContinuedFraction` [:math:`x`, :math:`n`]
    generate the first :math:`n` terms in the continued fraction representation of :math:`x`.

:code:`ContinuedFraction` [:math:`x`]
    the complete continued fraction representation for a rational or quadradic irrational number.





>>> ContinuedFraction[Pi, 10]
  = {3, 7, 15, 1, 292, 1, 1, 1, 2, 1}
>>> ContinuedFraction[(1 + 2 Sqrt[3])/5]
  = {0, 1, {8, 3, 34, 3}}
>>> ContinuedFraction[Sqrt[70]]
  = {8, {2, 1, 2, 1, 2, 16}}
