Positive
========

`WMA link <https://reference.wolfram.com/language/ref/Positive.html>`_


:code:`Positive` [:math:`x`]
    returns :code:`True`  if :math:`x` is a positive real number.





>>> Positive[1]
  = True

:code:`Positive`  returns :code:`False`  if :math:`x` is zero or a complex number:

>>> Positive[0]
  = False
>>> Positive[1 + 2 I]
  = False
