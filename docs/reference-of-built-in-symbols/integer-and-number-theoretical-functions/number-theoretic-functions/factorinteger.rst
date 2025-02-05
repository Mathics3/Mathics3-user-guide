FactorInteger
=============

`WMA link <https://reference.wolfram.com/language/ref/FactorInteger.html>`_


:code:`FactorInteger` [:math:`n`]
    returns the factorization of :math:`n` as a list of factors and exponents.





>>> factors = FactorInteger[2010]
  = {{2, 1}, {3, 1}, {5, 1}, {67, 1}}

To get back the original number:

>>> Times @@ Power @@@ factors
  = 2010

:code:`FactorInteger`  factors rationals using negative exponents:

>>> FactorInteger[2010 / 2011]
  = {{2, 1}, {3, 1}, {5, 1}, {67, 1}, {2011, -1}}
