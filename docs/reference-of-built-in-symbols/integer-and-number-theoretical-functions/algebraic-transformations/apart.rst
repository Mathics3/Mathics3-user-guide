Apart
=====

`WMA link <https://reference.wolfram.com/language/ref/Apart.html>`_


:code:`Apart` [:math:`expr`]
    writes :math:`expr` as a sum of individual fractions.

:code:`Apart` [:math:`expr`, :math:`var`]
    treats :math:`var` as the main variable.





>>> Apart[1 / (x^2 + 5x + 6)]
  = 1 / (2 + x) - 1 / (3 + x)

When several variables are involved, the results can be different
depending on the main variable:

>>> Apart[1 / (x^2 - y^2), x]
  = -1 / (2 y (x + y)) + 1 / (2 y (x - y))
>>> Apart[1 / (x^2 - y^2), y]
  = 1 / (2 x (x + y)) + 1 / (2 x (x - y))

:code:`Apart`  is :code:`Listable` :

>>> Apart[{1 / (x^2 + 5x + 6)}]
  = {1 / (2 + x) - 1 / (3 + x)}

But it does not touch other expressions:

>>> Sin[1 / (x ^ 2 - y ^ 2)] // Apart
  = Sin[1 / (x ^ 2 - y ^ 2)]
