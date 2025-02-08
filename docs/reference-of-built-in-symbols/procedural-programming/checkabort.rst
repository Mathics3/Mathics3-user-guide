CheckAbort
==========

`WMA link <https://reference.wolfram.com/language/ref/CheckAbort.html>`_


:code:`CheckAbort` [:math:`expr`, :math:`failexpr`]
    evaluates :math:`expr`, returning :math:`failexpr` if an abort occurs.





>>> CheckAbort[Abort[]; 1, 2] + x
    =

:math:`2+x`


>>> CheckAbort[1, 2] + x
    =

:math:`1+x`


