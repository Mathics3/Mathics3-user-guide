NumberDigit
===========

`WMA link <https://reference.wolfram.com/language/ref/NumberDigit.html>`_


:code:`NumberDigit` [:math:`x`, :math:`n`]
    returns the digit coefficient of 10^:math:`n` for the real-valued number :math:`x`.

:code:`NumberDigit` [:math:`x`, :math:`n`, :math:`b`]
    returns the coefficient of :math:`b`^:math:`n` in the base-:math:`b` representation of :math:`x`.





Get the 10^2 digit of a 210.345:

>>> NumberDigit[210.345, 2]
  = 2

Get the 10^-1 digit of a 210.345:

>>> NumberDigit[210.345, -1]
  = 3
>>> BaseForm[N[Pi], 2]
  = 11.00100100001111110_2

Get the 2^0 bit of the Pi:
= 1