Min
===

`WMA link <https://reference.wolfram.com/language/ref/Min.html>`_


:code:`Min` [:math:`e_1`, :math:`e_2`, ..., :math:`e_i`]
    returns the expression with the lowest value among the :math:`e_i`.





Minimum of a series of values:

>>> Min[4, -8, 1]
    =

:math:`-8`


>>> Min[E - Pi, Pi, E + Pi, 2 E]
    =

:math:`E- \pi`



:code:`Min`  flattens lists in its arguments:

>>> Min[{1,2},3,{-3,3.5,-Infinity},{{1/2}}]
    =

:math:`-\infty`



:code:`Min`  with symbolic arguments remains in symbolic form:

>>> Min[x, y]
    =

:math:`\text{Min}\left[x,y\right]`


>>> Min[5, x, -3, y, 40]
    =

:math:`\text{Min}\left[-3,x,y\right]`



With no arguments, :code:`Min`  gives :code:`Infinity` :

>>> Min[]
    =

:math:`\infty`


