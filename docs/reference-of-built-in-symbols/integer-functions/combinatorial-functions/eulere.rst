EulerE
======

`Euler numbers <https://en.wikipedia.org/wiki/Euler_numbers>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.numbers.euler>`_, `WMA <https://reference.wolfram.com/language/ref/EulerE.html>`_)

:code:`EulerE` [:math:`n`]
    Euler number :math:`E_n`.

:code:`EulerE` [:math:`n`, :math:`x`]
    Euler polynomial :math:`E_n(x)`.





Odd-index Euler numbers are zero:

>>> Table[EulerE[k], {k, 1, 9, 2}]
    =

:math:`\left\{0,0,0,0,0\right\}`



Even-index Euler numbers alternate in sign:

>>> Table[EulerE[k], {k, 0, 8, 2}]
    =

:math:`\left\{1,-1,5,-61,1385\right\}`


>>> EulerE[5, z]
    =

:math:`-\frac{1}{2}+\frac{5 z^2}{2}-\frac{5 z^4}{2}+z^5`


