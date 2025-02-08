IntegerDigits
=============

`WMA link <https://reference.wolfram.com/language/ref/IntegerDigits.html>`_


:code:`IntegerDigits` [:math:`n`]
    returns the decimal representation of integer :math:`x` as list of digits.           :math:`x`'s sign is ignored.

:code:`IntegerDigits` [:math:`n`, :math:`b`]
    returns the base :math:`b` representation of integer :math:`x` as list of digits.           :math:`x`'s sign is ignored.

:code:`IntegerDigits` [:math:`n`, :math:`b`, :math:`length`]
    returns a list of length :math:`length`. If the number is too short, the           list gets padded with 0 on the left. If the number is too long, the           :math:`length` least significant digits are returned.





>>> IntegerDigits[76543]
    =

:math:`\left\{7,6,5,4,3\right\}`



The same thing specifying base 10 explicitly:

>>> IntegerDigits[76543, 10]
    =

:math:`\left\{7,6,5,4,3\right\}`



The sign is discarded:

>>> IntegerDigits[-76543]
    =

:math:`\left\{7,6,5,4,3\right\}`



Just the last 3 digits:

>>> IntegerDigits[76543, 10, 3]
    =

:math:`\left\{5,4,3\right\}`



A geeky way to relate Christmas with Halloween is to note that     Dec(imal) 25 is Oct(al) 31

>>> IntegerDigits[25, 8]
    =

:math:`\left\{3,1\right\}`


