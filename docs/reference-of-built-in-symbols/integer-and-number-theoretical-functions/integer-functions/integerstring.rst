IntegerString
=============

`WMA link <https://reference.wolfram.com/language/ref/IntegerString.html>`_


:code:`IntegerString` [:math:`n`]
    returns the decimal representation of integer :math:`x` as string. :math:`x`'s sign is ignored.

:code:`IntegerString` [:math:`n`, :math:`b`]
    returns the base :math:`b` representation of integer :math:`x` as string. :math:`x`'s sign is ignored.

:code:`IntegerString` [:math:`n`, :math:`b`, :math:`length`]
    returns a string of length :math:`length`. If the number is too short, the string gets padded
    with 0 on the left. If the number is too long, the :math:`length` least significant digits are
    returned.





For bases > 10, alphabetic characters a, b, ... are used to represent digits 11, 12, ... . Note
that base must be an integer in the range from 2 to 36.

>>> IntegerString[12345]
  = 12345
>>> IntegerString[-500]
  = 500
>>> IntegerString[12345, 10, 8]
  = 00012345
>>> IntegerString[12345, 10, 3]
  = 345
>>> IntegerString[11, 2]
  = 1011
>>> IntegerString[123, 8]
  = 173
>>> IntegerString[32767, 16]
  = 7fff
>>> IntegerString[98765, 20]
  = c6i5
