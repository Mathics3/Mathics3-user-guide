FromDigits
==========

`WMA link <https://reference.wolfram.com/language/ref/FromDigits.html>`_


:code:`FromDigits` [:math:`l`]
    returns the integer corresponding to the decimal representation given by :math:`l`. :math:`l` can           be a list of digits or a string.

:code:`FromDigits` [:math:`l`, :math:`b`]
    returns the integer corresponding to the base :math:`b` representation given by :math:`l`. :math:`l` can           be a list of digits or a string.





>>> FromDigits["123"]

    =
:math:`123`


>>> FromDigits[{1, 2, 3}]

    =
:math:`123`


>>> FromDigits[{1, 0, 1}, 1000]

    =
:math:`1000001`



FromDigits can handle symbolic input:

>>> FromDigits[{a, b, c}, 5]

    =
:math:`c+5 \left(5 a+b\right)`



Note that FromDigits does not automatically detect if you are providing a non-decimal representation:

>>> FromDigits["a0"]

    =
:math:`100`


>>> FromDigits["a0", 16]

    =
:math:`160`



FromDigits on empty lists or strings returns 0:

>>> FromDigits[{}]

    =
:math:`0`


>>> FromDigits[""]

    =
:math:`0`


