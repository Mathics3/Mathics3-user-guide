$RecursionLimit
===============

`WMA link <https://reference.wolfram.com/language/ref/$RecursionLimit.html>`_


:code:`$RecursionLimit`
    specifies the maximum allowable recursion depth after which a calculation is terminated.





Calculations terminated by :code:`$RecursionLimit`  return :code:`$Aborted` :

>>> a = a + a
  = $Aborted
>>> $RecursionLimit
  = 200
>>> $RecursionLimit = x;

>>> $RecursionLimit = 512
  = 512
>>> a = a + a
  = $Aborted
