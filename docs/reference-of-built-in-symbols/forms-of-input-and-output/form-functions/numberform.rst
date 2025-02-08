NumberForm
==========

`WMA link <https://reference.wolfram.com/language/ref/NumberForm.html>`_


:code:`NumberForm` [:math:`expr`, :math:`n`]
    prints a real number :math:`expr` with :math:`n`-digits of precision.

:code:`NumberForm` [:math:`expr`, {:math:`n`, :math:`f`}]
    prints with :math:`n`-digits and :math:`f` digits to the right of the decimal point.





>>> NumberForm[N[Pi], 10]
    =

:math:`3.141592654`


>>> NumberForm[N[Pi], {10, 6}]
    =

:math:`3.141593`


>>> NumberForm[N[Pi]]
    =

:math:`3.14159`


