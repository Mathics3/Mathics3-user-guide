UnitStep
========

`Heaviside step function <https://en.wikipedia.org/wiki/Heaviside_step_function>`_ (`WMA link <https://reference.wolfram.com/language/ref/UnitStep.html>`_)


:code:`UnitStep` [:math:`x`]
    return 0 if :math:`x` < 0, and 1 if :math:`x` >= 0.

:code:`UnitStep` [:math:`x_1`, :math:`x_2`, ...]
    return the multidimensional unit step function which is 1 only if none of the :math:`xi` are negative.





Evaluation numerically:

>>> UnitStep[0.7]

    =
:math:`1`



We can use :code:`UnitStep`  on irrational numbers and infinities:

>>> Map[UnitStep, {Pi, Infinity, -Infinity}]

    =
:math:`\left\{1,1,0\right\}`


>>> Table[UnitStep[x], {x, -3, 3}]

    =
:math:`\left\{0,0,0,1,1,1,1\right\}`



Plot in one dimension:

>>> Plot[UnitStep[x], {x, -4, 4}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Numerical_Functions_UnitStep_569xy98n.png
    :align: center



