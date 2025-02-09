Inequality
==========

`WMA link <https://reference.wolfram.com/language/ref/Inequality.html>`_


:code:`Inequality`
    is the head of expressions involving different inequality
    operators (at least temporarily). Thus, it is possible to
    write chains of inequalities.





>>> a < b <= c

    =
:math:`a<b\text{\&\&}b\text{<=}c`


>>> Inequality[a, Greater, b, LessEqual, c]

    =
:math:`a>b\text{\&\&}b\text{<=}c`


>>> 1 < 2 <= 3

    =
:math:`\text{True}`


>>> 1 < 2 > 0

    =
:math:`\text{True}`


>>> 1 < 2 < -1

    =
:math:`\text{False}`


