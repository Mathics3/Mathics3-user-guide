Times
=====

`Multiplication <https://en.wikipedia.org/wiki/Multiplication>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.mul.Mul>`_, `WMA <https://reference.wolfram.com/language/ref/Times.html>`_)


:code:`Times` [:math:`a`, :math:`b`, ...]
    same as

:math:`a` :code:`*`  :math:`b` :code:`*`  ...
    same as

:math:`a` :math:`b` ...
    represents the product of the terms :math:`a`, :math:`b`, ...





>>> 10 * 2
  = 20
>>> 10 2
  = 20
>>> a * a
  = a ^ 2
>>> x ^ 10 * x ^ -2
  = x ^ 8
>>> {1, 2, 3} * 4
  = {4, 8, 12}
>>> Times @@ {1, 2, 3, 4}
  = 24
>>> IntegerLength[Times@@Range[5000]]
  = 16326

:code:`Times`  has default value 1:

>>> DefaultValues[Times]
  = {HoldPattern[Default[Times]] :> 1}
>>> a /. n_. * x_ :> {n, x}
  = {1, a}
