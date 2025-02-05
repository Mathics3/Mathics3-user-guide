ReleaseHold
===========

`WMA link <https://reference.wolfram.com/language/ref/ReleaseHold.html>`_


:code:`ReleaseHold` [:math:`expr`]
    removes any :code:`Hold` , :code:`HoldForm` , :code:`HoldPattern`  or
    :code:`HoldComplete`  head from :math:`expr`.





>>> x = 3;

>>> Hold[x]
  = Hold[x]
>>> ReleaseHold[Hold[x]]
  = 3
>>> ReleaseHold[y]
  = y
