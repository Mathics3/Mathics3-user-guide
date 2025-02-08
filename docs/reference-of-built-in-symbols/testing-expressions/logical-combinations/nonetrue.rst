NoneTrue
========

`WMA link <https://reference.wolfram.com/language/ref/NoneTrue.html>`_


:code:`NoneTrue` [{:math:`expr_1`, :math:`expr_2`, ...}, :math:`test`]
    returns True if no application of :math:`test` to :math:`expr_1`, :math:`expr_2`, ...           evaluates to True.

:code:`NoneTrue` [:math:`list`, :math:`test`, :math:`level`]
    returns True if no application of :math:`test` to items of :math:`list` at           :math:`level` evaluates to True.

:code:`NoneTrue` [:math:`test`]
    gives an operator that may be applied to expressions.





>>> NoneTrue[{1, 3, 5}, EvenQ]
    =

:math:`\text{True}`


>>> NoneTrue[{1, 4, 5}, EvenQ]
    =

:math:`\text{False}`


