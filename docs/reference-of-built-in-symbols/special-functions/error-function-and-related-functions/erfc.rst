Erfc
====

`Complementary Error function <https://en.wikipedia.org/wiki/Error_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.error_functions.erfc>`_, `WMA <https://reference.wolfram.com/language/ref/Erfc.html>`_)


:code:`Erfc` [:math:`z`]
    returns the complementary error function of :math:`z`.





>>> Erfc[-x] / 2
  = (2 - Erfc[x]) / 2
>>> Erfc[1.0]
  = 0.157299
>>> Erfc[0]
  = 1
>>> Plot[Erfc[x], {x, -2, 2}]
  = -Graphics-
