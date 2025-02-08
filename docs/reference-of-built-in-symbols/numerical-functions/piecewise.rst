Piecewise
=========

`SymPy <https://docs.sympy.org/latest/modules/functions/elementary.html#piecewise>`_, `WMA <https://reference.wolfram.com/language/ref/Piecewise.html>`_


:code:`Piecewise[{{expr1, cond1}, ...}]`
    represents a piecewise function.

:code:`Piecewise[{{expr1, cond1}, ...}, expr]`
    represents a piecewise function with default :code:`expr` .





Heaviside function

>>> Piecewise[{{0, x <= 0}}, 1]
    =

:math:`\text{Piecewise}\left[\left\{\left\{0,x\text{<=}0\right\}\right\},1\right]`


>>> Integrate[Piecewise[{{1, x <= 0}, {-1, x > 0}}], x]
    =

:math:`\text{Piecewise}\left[\left\{\left\{x,x\text{<=}0\right\}\right\},-x\right]`


>>> Integrate[Piecewise[{{1, x <= 0}, {-1, x > 0}}], {x, -1, 2}]
    =

:math:`-1`



Piecewise defaults to 0 if no other case is matching.

>>> Piecewise[{{1, False}}]
    =

:math:`0`


>>> Plot[Piecewise[{{Log[x], x > 0}, {x*-0.5, x < 0}}], {x, -1, 1}]
    =

.. image:: tmpgvbrhox6.png
    :align: center



>>> Piecewise[{{0 ^ 0, False}}, -1]
    =

:math:`-1`


