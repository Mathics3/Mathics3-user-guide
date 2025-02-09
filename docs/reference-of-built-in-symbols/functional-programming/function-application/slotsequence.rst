SlotSequence
============

`WMA link <https://reference.wolfram.com/language/ref/SlotSequence.html>`_



:code:`##`
    is the sequence of arguments supplied to a pure function.

:code:`##:math:`n``
    starts with the :math:`n`-th argument.





>>> Plus[##]& [1, 2, 3]

    =
:math:`6`


>>> Plus[##2]& [1, 2, 3]

    =
:math:`5`


>>> FullForm[##]

    =
:math:`\text{SlotSequence}\left[1\right]`


