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
  = {7, 6, 5, 4, 3}

The same thing specifying base 10 explicitly:

>>> IntegerDigits[76543, 10]
  = {7, 6, 5, 4, 3}

The sign is discarded:

>>> IntegerDigits[-76543]
  = {7, 6, 5, 4, 3}

Just the last 3 digits:

>>> IntegerDigits[76543, 10, 3]
  = {5, 4, 3}

A geeky way to relate Christmas with Halloween is to note that     Dec(imal) 25 is Oct(al) 31

>>> IntegerDigits[25, 8]
  = {3, 1}
