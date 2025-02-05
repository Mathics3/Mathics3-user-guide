SlotSequence
============

`WMA link <https://reference.wolfram.com/language/ref/SlotSequence.html>`_



:code:`##`
    is the sequence of arguments supplied to a pure function.

:code:`##:math:`n``
    starts with the :math:`n`-th argument.





>>> Plus[##]& [1, 2, 3]
  = 6
>>> Plus[##2]& [1, 2, 3]
  = 5
>>> FullForm[##]
  = SlotSequence[1]
