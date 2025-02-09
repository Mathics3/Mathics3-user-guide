MatchQ
======

`WMA link <https://reference.wolfram.com/language/ref/MatchQ.html>`_


:code:`MatchQ` [:math:`expr`, :math:`form`]
    tests whether :math:`expr` matches :math:`form`.





>>> MatchQ[123, _Integer]

    =
:math:`\text{True}`


>>> MatchQ[123, _Real]

    =
:math:`\text{False}`


>>> MatchQ[_Integer][123]

    =
:math:`\text{True}`


>>> MatchQ[3, Pattern[3]]

    Pattern::patvar First element in pattern Pattern[3] is not a valid pattern name.

    =
:math:`\text{False}`


