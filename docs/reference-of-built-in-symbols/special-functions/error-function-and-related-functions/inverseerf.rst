InverseErf
==========

`Inverse error function <https://en.wikipedia.org/wiki/Error_function#Inverse_functions>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html?sympy.functions.special.error_functions.erfinv>`_, `WMA <https://reference.wolfram.com/language/ref/InverseErf.html>`_)


:code:`InverseErf` [:math:`z`]
    returns the inverse error function of :math:`z`.





>>> InverseErf /@ {-1, 0, 1}
  = {-Infinity, 0, Infinity}
>>> Plot[InverseErf[x], {x, -1, 1}]
  = -Graphics-

:code:`InverseErf[:math:`z`]`  only returns numeric values for :code:`-1 <= :math:`z` <= 1` :

>>> InverseErf /@ {0.9, 1.0, 1.1}
  = {1.16309, Infinity, InverseErf[1.1]}
