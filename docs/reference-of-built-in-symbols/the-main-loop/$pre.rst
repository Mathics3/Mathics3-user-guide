$Pre
====

`WMA <https://reference.wolfram.com/language/ref/$Pre>`_

:code:`$Pre`
    is a global variable whose value, if set, is applied to every input expression.





Set :code:`Timing`  as the :code:`$Pre`  function, stores the elapsed time in a variable,
stores just the result in :code:`Out[$Line]`  and print a formatted version showing the elapsed time

>>> $Pre := (Print["[Processing input...]"];#1)&

>>> $Post := (Print["[Storing result...]"]; #1)&

>>> $PrePrint := (Print["The result is:"]; {TimeUsed[], #1})&

>>> 2 + 2
  = {..., 4}
>>> $Pre = .; $Post = .;  $PrePrint = .;  $ElapsedTime = .;

>>> 2 + 2
  = 4
