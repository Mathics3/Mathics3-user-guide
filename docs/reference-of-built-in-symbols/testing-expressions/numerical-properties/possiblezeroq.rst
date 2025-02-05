PossibleZeroQ
=============

`WMA link <https://reference.wolfram.com/language/ref/PossibleZeroQ.html>`_


:code:`PossibleZeroQ` [:math:`expr`]
    returns :code:`True`  if basic symbolic and numerical methods suggest that           expr has value zero, and :code:`False`  otherwise.





Test whether a numeric expression is zero:

>>> PossibleZeroQ[E^(I Pi/4) - (-1)^(1/4)]
  = True

The determination is approximate.

Test whether a symbolic expression is likely to be identically zero:

>>> PossibleZeroQ[(x + 1) (x - 1) - x^2 + 1]
  = True
>>> PossibleZeroQ[(E + Pi)^2 - E^2 - Pi^2 - 2 E Pi]
  = True

Show that a numeric expression is nonzero:

>>> PossibleZeroQ[E^Pi - Pi^E]
  = False
>>> PossibleZeroQ[1/x + 1/y - (x + y)/(x y)]
  = True

Decide that a numeric expression is zero, based on approximate computations:

>>> PossibleZeroQ[2^(2 I) - 2^(-2 I) - 2 I Sin[Log[4]]]
  = True
>>> PossibleZeroQ[Sqrt[x^2] - x]
  = False
