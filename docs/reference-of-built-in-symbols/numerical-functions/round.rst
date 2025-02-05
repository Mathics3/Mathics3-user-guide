Round
=====

`WMA link <https://reference.wolfram.com/language/ref/Round.html>`_


:code:`Round` [:math:`expr`]
    rounds :math:`expr` to the nearest integer.

:code:`Round` [:math:`expr`, :math:`k`]
    rounds :math:`expr` to the closest multiple of :math:`k`.





>>> Round[10.6]
  = 11
>>> Round[0.06, 0.1]
  = 0.1
>>> Round[0.04, 0.1]
  = 0.

Constants can be rounded too

>>> Round[Pi, .5]
  = 3.
>>> Round[Pi^2]
  = 10

Round to exact value

>>> Round[2.6, 1/3]
  = 8 / 3
>>> Round[10, Pi]
  = 3 Pi

Round complex numbers

>>> Round[6/(2 + 3 I)]
  = 1 - I
>>> Round[1 + 2 I, 2 I]
  = 2 I

Round Negative numbers too

>>> Round[-1.4]
  = -1

Expressions other than numbers remain unevaluated:

>>> Round[x]
  = Round[x]
>>> Round[1.5, k]
  = Round[1.5, k]
