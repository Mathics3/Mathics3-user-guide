$TraceEvaluation
================


:code:`$TraceEvaluation`
    A Boolean variable which when set True traces Expression evaluation calls and returns.





>>> $TraceEvaluation = True
  = True
>>> a + a
  = 2 a

Setting it to :code:`False`  again recovers the normal behaviour:

>>> $TraceEvaluation = False
  = False
>>> $TraceEvaluation
  = False
>>> a + a
  = 2 a

:code:`$TraceEvaluation`  cannot be set to a non-boolean value.

>>> $TraceEvaluation = x
  = x
