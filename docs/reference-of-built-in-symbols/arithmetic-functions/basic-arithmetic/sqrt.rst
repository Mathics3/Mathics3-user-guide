Sqrt
====

`Square root <https://en.wikipedia.org/wiki/Square_root>`_ (`SymPy <https://docs.sympy.org/latest/modules/codegen.html#sympy.codegen.cfunctions.Sqrt>`_, `WMA <https://reference.wolfram.com/language/ref/Sqrt.html>`_)


:code:`Sqrt` [:math:`expr`]
    returns the square root of :math:`expr`.





>>> Sqrt[4]
  = 2
>>> Sqrt[5]
  = Sqrt[5]
>>> Sqrt[5] // N
  = 2.23607
>>> Sqrt[a]^2
  = a

Complex numbers:

>>> Sqrt[-4]
  = 2 I
>>> I == Sqrt[-1]
  = True
>>> Plot[Sqrt[a^2], {a, -2, 2}]
  = -Graphics-
