Together
========

`WMA link <https://reference.wolfram.com/language/ref/Together.html>`_


:code:`Together` [:math:`expr`]
    writes sums of fractions in :math:`expr` together.





>>> Together[a / c + b / c]
  = (a + b) / c

:code:`Together`  operates on lists:

>>> Together[{x / (y+1) + x / (y+1)^2}]
  = {x (2 + y) / (1 + y) ^ 2}

But it does not touch other functions:

>>> Together[f[a / c + b / c]]
  = f[a / c + b / c]
