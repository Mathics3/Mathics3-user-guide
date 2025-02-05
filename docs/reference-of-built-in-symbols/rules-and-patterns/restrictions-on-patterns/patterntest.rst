PatternTest
===========

`WMA link <https://reference.wolfram.com/language/ref/PatternTest.html>`_


:code:`PatternTest` [:math:`pattern`, :math:`test`]
    same as

:code:`:math:`pattern` ? :math:`test``
    constrains :math:`pattern` to match :math:`expr` only if the           evaluation of :code:`:math:`test`[:math:`expr`]`  yields :code:`True` .





>>> MatchQ[3, _Integer?(#>0&)]
  = True
>>> MatchQ[-3, _Integer?(#>0&)]
  = False
>>> MatchQ[3, Pattern[3]]
  = False
