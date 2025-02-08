MinimalPolynomial
=================

`WMA link <https://reference.wolfram.com/language/ref/MinimalPolynomial.html>`_


:code:`MinimalPolynomial[s, x]`
    gives the minimal polynomial in :math:`x` for which the algebraic       number :math:`s` is a root.





>>> MinimalPolynomial[7, x]
    =

:math:`-7+x`


>>> MinimalPolynomial[Sqrt[2] + Sqrt[3], x]
    =

:math:`1-10 x^2+x^4`


>>> MinimalPolynomial[Sqrt[1 + Sqrt[3]], x]
    =

:math:`-2-2 x^2+x^4`


>>> MinimalPolynomial[Sqrt[I + Sqrt[6]], x]
    =

:math:`49-10 x^4+x^8`


