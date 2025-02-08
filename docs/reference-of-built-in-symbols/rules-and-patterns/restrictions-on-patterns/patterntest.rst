PatternTest
===========

`WMA link <https://reference.wolfram.com/language/ref/PatternTest.html>`_


:code:`PatternTest` [:math:`pattern`, :math:`test`]
    same as

:code:`:math:`pattern` ? :math:`test``
    constrains :math:`pattern` to match :math:`expr` only if the           evaluation of :code:`:math:`test`[:math:`expr`]`  yields :code:`True` .





>>> MatchQ[3, _Integer?(#>0&)]
    =

:math:`\text{True}`


>>> MatchQ[-3, _Integer?(#>0&)]
    =

:math:`\text{False}`


>>> MatchQ[3, Pattern[3]]

    Pattern::patvar First element in pattern Pattern[3] is not a valid pattern name.
    =

:math:`\text{False}`


