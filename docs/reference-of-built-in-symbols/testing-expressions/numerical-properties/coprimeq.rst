CoprimeQ
========

`WMA link <https://reference.wolfram.com/language/ref/CoprimeQ.html>`_


:code:`CoprimeQ` [:math:`x`, :math:`y`]
    tests whether :math:`x` and :math:`y` are coprime by computing their greatest           common divisor.





>>> CoprimeQ[7, 9]
  = True
>>> CoprimeQ[-4, 9]
  = True
>>> CoprimeQ[12, 15]
  = False

For more than two arguments, CoprimeQ checks if any pair or arguments are coprime:

>>> CoprimeQ[2, 3, 5]
  = True

In this case, since 2 divides 4, the result is False:

>>> CoprimeQ[2, 4, 5]
  = False
