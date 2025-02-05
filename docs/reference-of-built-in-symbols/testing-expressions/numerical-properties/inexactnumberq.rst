InexactNumberQ
==============

`WMA link <https://reference.wolfram.com/language/ref/InexactNumberQ.html>`_


:code:`InexactNumberQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is not an exact real or complex number
    number, and :code:`False`  otherwise.





>>> InexactNumberQ[a]
  = False
>>> InexactNumberQ[3.0]
  = True
>>> InexactNumberQ[2/3]
  = False

:code:`InexactNumberQ`  is :code:`True`  for complex numbers:

>>> InexactNumberQ[4.0+I]
  = True
