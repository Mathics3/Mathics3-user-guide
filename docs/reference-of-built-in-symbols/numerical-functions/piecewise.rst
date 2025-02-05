Piecewise
=========

`SymPy <https://docs.sympy.org/latest/modules/functions/elementary.html#piecewise>`_, `WMA <https://reference.wolfram.com/language/ref/Piecewise.html>`_


:code:`Piecewise[{{expr1, cond1}, ...}]`
    represents a piecewise function.

:code:`Piecewise[{{expr1, cond1}, ...}, expr]`
    represents a piecewise function with default :code:`expr` .





Heaviside function

>>> Piecewise[{{0, x <= 0}}, 1]
  = Piecewise[{{0, x <= 0}}, 1]
>>> Integrate[Piecewise[{{1, x <= 0}, {-1, x > 0}}], x]
  = Piecewise[{{x, x <= 0}}, -x]
>>> Integrate[Piecewise[{{1, x <= 0}, {-1, x > 0}}], {x, -1, 2}]
  = -1

Piecewise defaults to 0 if no other case is matching.

>>> Piecewise[{{1, False}}]
  = 0
>>> Plot[Piecewise[{{Log[x], x > 0}, {x*-0.5, x < 0}}], {x, -1, 1}]
  = -Graphics-
>>> Piecewise[{{0 ^ 0, False}}, -1]
  = -1
