MatchQ
======

`WMA link <https://reference.wolfram.com/language/ref/MatchQ.html>`_


:code:`MatchQ` [:math:`expr`, :math:`form`]
    tests whether :math:`expr` matches :math:`form`.





>>> MatchQ[123, _Integer]
  = True
>>> MatchQ[123, _Real]
  = False
>>> MatchQ[_Integer][123]
  = True
>>> MatchQ[3, Pattern[3]]
  = False
