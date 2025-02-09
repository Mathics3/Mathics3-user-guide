AnyTrue
=======

`WMA link <https://reference.wolfram.com/language/ref/AnyTrue.html>`_


:code:`AnyTrue` [{:math:`expr_1`, :math:`expr_2`, ...}, :math:`test`]
    returns True if any application of :math:`test` to           :math:`expr_1`, :math:`expr_2`, ... evaluates to True.

:code:`AnyTrue` [:math:`list`, :math:`test`, :math:`level`]
    returns True if any application of :math:`test` to items of           :math:`list` at :math:`level` evaluates to True.

:code:`AnyTrue` [:math:`test`]
    gives an operator that may be applied to expressions.





>>> AnyTrue[{1, 3, 5}, EvenQ]

    =
:math:`\text{False}`


>>> AnyTrue[{1, 4, 5}, EvenQ]

    =
:math:`\text{True}`


