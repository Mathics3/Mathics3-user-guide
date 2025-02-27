Chop
====

`WMA link <https://reference.wolfram.com/language/ref/Chop.html>`_


:code:`Chop` [:math:`expr`]
    replaces floating point numbers close to 0 by 0.

:code:`Chop` [:math:`expr`, :math:`delta`]
    uses a tolerance of :math:`delta`. The default tolerance is :code:`10^-10` .





>>> Chop[10.0 ^ -16]

    =
:math:`0`


>>> Chop[10.0 ^ -9]

    =
:math:`1.\text{*${}^{\wedge}$}-9`


>>> Chop[10 ^ -11 I]

    =
:math:`\frac{I}{100000000000}`


>>> Chop[0. + 10 ^ -11 I]

    =
:math:`0`


