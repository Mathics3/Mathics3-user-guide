Min
===

`WMA link <https://reference.wolfram.com/language/ref/Min.html>`_


:code:`Min` [:math:`e_1`, :math:`e_2`, ..., :math:`e_i`]
    returns the expression with the lowest value among the :math:`e_i`.





Minimum of a series of values:

>>> Min[4, -8, 1]
  = -8
>>> Min[E - Pi, Pi, E + Pi, 2 E]
  = E - Pi

:code:`Min`  flattens lists in its arguments:

>>> Min[{1,2},3,{-3,3.5,-Infinity},{{1/2}}]
  = -Infinity

:code:`Min`  with symbolic arguments remains in symbolic form:

>>> Min[x, y]
  = Min[x, y]
>>> Min[5, x, -3, y, 40]
  = Min[-3, x, y]

With no arguments, :code:`Min`  gives :code:`Infinity` :

>>> Min[]
  = Infinity
