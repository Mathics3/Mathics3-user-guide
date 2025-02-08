$Pre
====

`WMA <https://reference.wolfram.com/language/ref/$Pre>`_

:code:`$Pre`
    is a global variable whose value, if set, is applied to every input expression.





Set :code:`Timing`  as the :code:`$Pre`  function, stores the elapsed time in a variable,
stores just the result in :code:`Out[$Line]`  and print a formatted version showing the elapsed time

>>> $Pre := (Print["[Processing input...]"];#1)&


>>> $Post := (Print["[Storing result...]"]; #1)&

    [Processing input...]

    [Storing result...]


>>> $PrePrint := (Print["The result is:"]; {TimeUsed[], #1})&

    [Processing input...]

    [Storing result...]


>>> 2 + 2

    [Processing input...]

    [Storing result...]

    The result is:
    =

:math:`\left\{261.137,4\right\}`


>>> $Pre = .; $Post = .;  $PrePrint = .;  $ElapsedTime = .;

    [Processing input...]


>>> 2 + 2
    =

:math:`4`


