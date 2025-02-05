UnitStep
========

`Heaviside step function <https://en.wikipedia.org/wiki/Heaviside_step_function>`_ (`WMA link <https://reference.wolfram.com/language/ref/UnitStep.html>`_)


:code:`UnitStep` [:math:`x`]
    return 0 if :math:`x` < 0, and 1 if :math:`x` >= 0.

:code:`UnitStep` [:math:`x_1`, :math:`x_2`, ...]
    return the multidimensional unit step function which is 1 only if none of the :math:`xi` are negative.





Evaluation numerically:

>>> UnitStep[0.7]
  = 1

We can use :code:`UnitStep`  on irrational numbers and infinities:

>>> Map[UnitStep, {Pi, Infinity, -Infinity}]
  = {1, 1, 0}
>>> Table[UnitStep[x], {x, -3, 3}]
  = {0, 0, 0, 1, 1, 1, 1}

Plot in one dimension:

>>> Plot[UnitStep[x], {x, -4, 4}]
  = -Graphics-
