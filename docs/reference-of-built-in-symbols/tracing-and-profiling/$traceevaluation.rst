$TraceEvaluation
================


:code:`$TraceEvaluation`
    A Boolean variable which when set True traces Expression evaluation calls and returns.





>>> $TraceEvaluation = True
    =

:math:`\text{True}`


>>> a + a
    =

:math:`2 a`



Setting it to :code:`False`  again recovers the normal behaviour:

>>> $TraceEvaluation = False
    =

:math:`\text{False}`


>>> $TraceEvaluation
    =

:math:`\text{False}`


>>> a + a
    =

:math:`2 a`



:code:`$TraceEvaluation`  cannot be set to a non-boolean value.

>>> $TraceEvaluation = x

    $TraceEvaluation::bool x should be True or False.
    =

:math:`x`


