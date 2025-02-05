Infinity
========

`
Infinity <https://en.wikipedia.org/wiki/Infinity>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.numbers.Infinity>`_, `WMA <https://reference.wolfram.com/language/ref/Infinity.html>`_)


:code:`Infinity`
    a symbol that represents an infinite real quantity.





:code:`Infinity`  sometimes appears as the result of a calculation:

>>> Precision[1]
  = Infinity

But :code:`Infinity`  it often used as a value in expressions:

>>> 1 / Infinity
  = 0
>>> Infinity + 100
  = Infinity

:code:`Infinity`  often appears in sum and limit calculations:

>>> Sum[1/x^2, {x, 1, Infinity}]
  = Pi ^ 2 / 6
>>> Limit[1/x, x->0]
  = -Infinity

However, :code:`Infinity`  a shorthand for :code:`DirectedInfinity[1]` :

>>> FullForm[Infinity]
  = DirectedInfinity[1]

See also `:code:`DirectedInfinity`  </doc/reference-of-built-in-symbols/mathematical-functions/directedinfinity/>`_.