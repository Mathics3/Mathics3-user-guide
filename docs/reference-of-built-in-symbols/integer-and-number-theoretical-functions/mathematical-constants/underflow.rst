Underflow
=========

`Arithmetic underflow <https://en.wikipedia.org/wiki/Arithmetic_underflow>`_ (`WMA <https://reference.wolfram.com/language/ref/Underflow.html>`_)


:code:`Overflow[]`
    represents a number too small to be represented by Mathics.





>>> 1 / Overflow[]
    =

:math:`\text{Underflow}\left[\right]`


>>> 5 * Underflow[]
    =

:math:`5 \text{Underflow}\left[\right]`


>>> % // N
    =

:math:`0.`



Underflow[] is kept symbolic in operations against integer numbers,
but taken as 0. in numeric evaluations:

>>> 1 - Underflow[]
    =

:math:`1-\text{Underflow}\left[\right]`


>>> % // N
    =

:math:`1.`


