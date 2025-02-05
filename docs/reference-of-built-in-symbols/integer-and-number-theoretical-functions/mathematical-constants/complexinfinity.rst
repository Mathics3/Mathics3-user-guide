ComplexInfinity
===============

`Complex Infinity <https://en.wikipedia.org/wiki/Infinity#Complex_analysis>`_     is an infinite number in the complex plane whose complex argument     is unknown or undefined. (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.numbers.ComplexInfinity>`_, `MathWorld <https://mathworld.wolfram.com/ComplexInfinity.html>`_, `WMA <https://reference.wolfram.com/language/ref/ComplexInfinity.html>`_)


:code:`ComplexInfinity`
    represents an infinite complex quantity of undetermined direction.





ComplexInfinity can appear as the result of a computation such as dividing by zero:

>>> 1 / 0
  = ComplexInfinity

But it can be used as an explicit value in an expression:

>>> 1 / ComplexInfinity
  = 0
>>> ComplexInfinity * Infinity
  = ComplexInfinity

ComplexInfinity though is a special case of DirectedInfinity:

>>> FullForm[ComplexInfinity]
  = DirectedInfinity[]

See also `:code:`DirectedInfinity`  </doc/reference-of-built-in-symbols/mathematical-functions/directedinfinity/>`_.