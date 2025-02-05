Erf
===

`Error function <https://en.wikipedia.org/wiki/Error_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.error_functions.erf>`_, `WMA <https://reference.wolfram.com/language/ref/Erf.html>`_)


:code:`Erf` [:math:`z`]
    returns the error function of :math:`z`.

:code:`Erf` [:math:`z_0`, :math:`z_1`]
    returns the result of :code:`Erf[:math:`z_1`] - Erf[:math:`z_0`]` .





:code:`Erf[:math:`x`]`  is an odd function:

>>> Erf[-x]
  = -Erf[x]
>>> Erf[1.0]
  = 0.842701
>>> Erf[0]
  = 0
>>> {Erf[0, x], Erf[x, 0]}
  = {Erf[x], -Erf[x]}
>>> Plot[Erf[x], {x, -2, 2}]
  = -Graphics-
