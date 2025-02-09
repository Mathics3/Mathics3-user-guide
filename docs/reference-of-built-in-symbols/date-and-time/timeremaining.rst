TimeRemaining
=============

`WMA link <https://reference.wolfram.com/language/ref/TimeRemaining.html>`_


:code:`TimeRemaining[]`
    Gives the number of seconds remaining until the earliest enclosing           :code:`TimeConstrained`  will request the current computation to stop.

:code:`TimeConstrained` [:math:`expr`, :math:`t`, :math:`failexpr`]
    returns :math:`failexpr` if the time constraint is not met.





If TimeConstrained is called out of a TimeConstrained expression, returns :code:`Infinity` :

>>> TimeRemaining[]

    =
:math:`\infty`


>>> TimeConstrained[1+2; Print[TimeRemaining[]], 0.9]

    0.899221


