TraceEvaluation
===============


:code:`TraceEvaluation` [:math:`expr`]
    Evaluate :math:`expr` and print each step of the evaluation.





The :code:`ShowTimeBySteps`  option prints the elapsed time before an evaluation occurs.

>>> TraceEvaluation[(x + x)^2]
    =

:math:`4 x^2`


>>> TraceEvaluation[(x + x)^2, ShowTimeBySteps->True]
    =

:math:`4 x^2`


