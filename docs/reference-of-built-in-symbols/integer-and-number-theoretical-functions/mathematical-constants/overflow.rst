Overflow
========

Numeric Overflow (`WMA <https://reference.wolfram.com/language/ref/Overflow.html>`_)

See also `Integer Overflow <https://en.wikipedia.org/wiki/Integer_overflow>`_.


:code:`Overflow[]`
    represents a number too large to be represented by Mathics.





>>> Exp[10.*^20]

    General::ovfl Overflow occurred in computation.

    =
:math:`\text{Overflow}\left[\right]`


>>> Table[Exp[10.^k],{k, 3}]

    General::ovfl Overflow occurred in computation.

    =
:math:`\left\{22026.5,2.68812\text{*${}^{\wedge}$}43,\text{Overflow}\left[\right]\right\}`


>>> 1 / Underflow[]

    =
:math:`\text{Overflow}\left[\right]`


