$RecursionLimit
===============

`WMA link <https://reference.wolfram.com/language/ref/$RecursionLimit.html>`_


:code:`$RecursionLimit`
    specifies the maximum allowable recursion depth after which a calculation is terminated.





Calculations terminated by :code:`$RecursionLimit`  return :code:`$Aborted` :

>>> a = a + a

    $RecursionLimit::reclim Recursion depth of 200 exceeded.

    =
:math:`\text{\$Aborted}`


>>> $RecursionLimit

    =
:math:`200`


>>> $RecursionLimit = x;

    $RecursionLimit::limset Cannot set $RecursionLimit to x; value must be an integer between 20 and 512; use the MATHICS_MAX_RECURSION_DEPTH environment variable to allow higher limits.


>>> $RecursionLimit = 512

    =
:math:`512`


>>> a = a + a

    $RecursionLimit::reclim Recursion depth of 512 exceeded.

    =
:math:`\text{\$Aborted}`


