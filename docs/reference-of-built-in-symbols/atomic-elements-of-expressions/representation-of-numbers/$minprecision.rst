$MinPrecision
=============

`WMA link <https://reference.wolfram.com/language/ref/$MinPrecision.html>`_


:code:`$MinPrecision`
    represents the minimum number of digits of precision permitted in abitrary-precision numbers.





>>> $MinPrecision
    =

:math:`0`


>>> $MinPrecision = 10;


>>> N[Pi, 9]

    N::precsm Requested precision 9 is smaller than $MinPrecision. Using current $MinPrecision of 10. instead.
    =

:math:`3.141592654`


