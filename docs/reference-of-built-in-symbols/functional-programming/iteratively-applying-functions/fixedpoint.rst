FixedPoint
==========

`WMA link <https://reference.wolfram.com/language/ref/FixedPoint.html>`_


:code:`FixedPoint` [:math:`f`, :math:`expr`]
    starting with :math:`expr`, iteratively applies :math:`f` until the result no longer changes.

:code:`FixedPoint` [:math:`f`, :math:`expr`, :math:`n`]
    performs at most :math:`n` iterations. The same that using :math:`MaxIterations->n`





>>> FixedPoint[Cos, 1.0]
    =

:math:`0.739085`


>>> FixedPoint[#+1 &, 1, 20]
    =

:math:`21`


