Pi
==

`Pi, π <https://en.wikipedia.org/wiki/Pi>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.numbers.Pi>`_, `WMA <https://reference.wolfram.com/language/ref/Pi.html>`_)


:code:`Pi`
    is the constant π.





>>> Pi
    =

:math:`\pi`


>>> N[Pi]
    =

:math:`3.14159`



Pi to a numeric precision of 20 digits:

>>> N[Pi, 20]
    =

:math:`3.1415926535897932385`



Note that the above is not the same thing as the number of digits *after* the decimal point. This may differ from similar concepts from other mathematical libraries, including those which Mathics uses!

Use numpy to compute Pi to 20 digits:

>>> N[Pi, 20, Method->"numpy"]
    =

:math:`3.1415926535897930000`



"sympy" is the default method.

>>> Attributes[Pi]
    =

:math:`\left\{\text{Constant},\text{Protected},\text{ReadProtected}\right\}`


