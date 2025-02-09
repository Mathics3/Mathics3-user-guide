ExactNumberQ
============

`WMA link <https://reference.wolfram.com/language/ref/ExactNumberQ.html>`_


:code:`ExactNumberQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is an exact real or complex number, and returns
    :code:`False`  otherwise.





>>> ExactNumberQ[10]

    =
:math:`\text{True}`



:code:`ExactNumber[]`  of a Real or MachineReal is :code:`False` 

>>> ExactNumberQ[10.0]

    =
:math:`\text{False}`



:code:`ExactNumberQ`  for complex numbers:

>>> ExactNumberQ[I]

    =
:math:`\text{True}`


>>> ExactNumberQ[1 + I]

    =
:math:`\text{True}`



but not when composed with a Real:

>>> ExactNumberQ[1. + I]

    =
:math:`\text{False}`



:code:`ExactNumber[]`  is :code:`True`  for Rational numbers:

>>> ExactNumberQ[5/6]

    =
:math:`\text{True}`


>>> ExactNumberQ[4 * I + 5/6]

    =
:math:`\text{True}`


