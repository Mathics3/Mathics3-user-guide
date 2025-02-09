MaxRecursion
============

`WMA link <https://reference.wolfram.com/language/ref/MaxRecursion.html>`_


:code:`MaxRecursion`
    is an option for functions like NIntegrate and Plot that specifies how many           recursive subdivisions can be made.





>>> NIntegrate[Exp[-10^8 x^2], {x, -1, 1}, Method->"Internal", MaxRecursion -> 3]

    =
:math:`0.0777778`


>>> NIntegrate[Exp[-10^8 x^2], {x, -1, 1}, Method->"Internal", MaxRecursion -> 6]

    =
:math:`0.00972222`


