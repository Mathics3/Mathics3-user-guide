RealDigits
==========

`WMA link <https://reference.wolfram.com/language/ref/RealDigits.html>`_


:code:`RealDigits` [:math:`n`]
    returns the decimal representation for the real number :math:`n` as list       of digits, together with the number of digits that are to the left of       the decimal point.

:code:`RealDigits` [:math:`n`, :math:`b`]
    returns a list of the "digits" in base-b representation for the real number :math:`n`.

:code:`RealDigits` [:math:`n`, :math:`b`, :math:`len`]
    returns a list of :math:`len` digits.

:code:`RealDigits` [:math:`n`, :math:`b`, :math:`len`, :math:`p`]
    return :math:`len` digits starting with the coefficient of :math:`b^p`.





Return the list of digits and exponent:

>>> RealDigits[123.55555]
  = {{1, 2, 3, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0}, 3}

Return an explicit recurring decimal form:

>>> RealDigits[19 / 7]
  = {{2, {7, 1, 4, 2, 8, 5}}, 1}

The 500th digit of Pi is 2:

>>> RealDigits[Pi, 10, 1, -500]
  = {{2}, -499}

11 digits starting with the coefficient of 10^-3:

>>> RealDigits[Pi, 10, 11, -3]
  = {{1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7}, -2}

RealDigits gives Indeterminate if more digits than the precision are requested:

>>> RealDigits[123.45, 10, 18]
  = {{1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Indeterminate, Indeterminate}, 3}

Return 25 digits of in base 10:

>>> RealDigits[Pi, 10, 25]
  = {{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3}, 1}
>>> RealDigits[10]
  = {{1, 0}, 2}
