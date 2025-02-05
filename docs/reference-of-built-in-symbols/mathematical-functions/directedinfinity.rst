DirectedInfinity
================

`WMA link <https://reference.wolfram.com/language/ref/DirectedInfinity.html>`_


:code:`DirectedInfinity` [:math:`z`]
    represents an infinite multiple of the complex number :math:`z`.

:code:`DirectedInfinity[]`
    is the same as :code:`ComplexInfinity` .





>>> DirectedInfinity[1]
  = Infinity
>>> DirectedInfinity[]
  = ComplexInfinity
>>> DirectedInfinity[1 + I]
  = (1 / 2 + I / 2) Sqrt[2] Infinity
>>> 1 / DirectedInfinity[1 + I]
  = 0
>>> DirectedInfinity[1] + DirectedInfinity[-1]
  = Indeterminate
>>> DirectedInfinity[0]
  = ComplexInfinity
