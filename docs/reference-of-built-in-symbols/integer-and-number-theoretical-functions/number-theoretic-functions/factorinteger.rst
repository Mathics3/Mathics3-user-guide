FactorInteger
=============

`WMA link <https://reference.wolfram.com/language/ref/FactorInteger.html>`_


:code:`FactorInteger` [:math:`n`]
    returns the factorization of :math:`n` as a list of factors and exponents.





>>> factors = FactorInteger[2010]

    =
:math:`\left\{\left\{2,1\right\},\left\{3,1\right\},\left\{5,1\right\},\left\{67,1\right\}\right\}`



To get back the original number:

>>> Times @@ Power @@@ factors

    =
:math:`2010`



:code:`FactorInteger`  factors rationals using negative exponents:

>>> FactorInteger[2010 / 2011]

    =
:math:`\left\{\left\{2,1\right\},\left\{3,1\right\},\left\{5,1\right\},\left\{67,1\right\},\left\{2011,-1\right\}\right\}`


