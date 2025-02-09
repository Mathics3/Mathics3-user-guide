IntegerLength
=============

`WMA link <https://reference.wolfram.com/language/ref/IntegerLength.html>`_


:code:`IntegerLength` [:math:`x`]
    gives the number of digits in the base-10 representation of :math:`x`.

:code:`IntegerLength` [:math:`x`, :math:`b`]
    gives the number of base-:math:`b` digits in :math:`x`.





>>> IntegerLength[123456]

    =
:math:`6`


>>> IntegerLength[10^10000]

    =
:math:`10001`


>>> IntegerLength[-10^1000]

    =
:math:`1001`



:code:`IntegerLength`  with base 2:

>>> IntegerLength[8, 2]

    =
:math:`4`



Check that :code:`IntegerLength`  is correct for the first 100 powers of 10:

>>> IntegerLength /@ (10 ^ Range[100]) == Range[2, 101]

    =
:math:`\text{True}`



The base must be greater than 1:

>>> IntegerLength[3, -2]

    IntegerLength::base Base -2 is not an integer greater than 1.

    =
:math:`\text{IntegerLength}\left[3,-2\right]`



:code:`0`  is a special case:

>>> IntegerLength[0]

    =
:math:`0`


