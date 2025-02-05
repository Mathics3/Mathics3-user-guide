MantissaExponent
================

`WMA link <https://reference.wolfram.com/language/ref/MantissaExponent.html>`_


:code:`MantissaExponent` [:math:`n`]
    finds a list containing the mantissa and exponent of a given number :math:`n`.

:code:`MantissaExponent` [:math:`n`, :math:`b`]
    finds the base b mantissa and exponent of :math:`n`.





>>> MantissaExponent[2.5*10^20]
  = {0.25, 21}
>>> MantissaExponent[125.24]
  = {0.12524, 3}
>>> MantissaExponent[125., 2]
  = {0.976563, 7}
>>> MantissaExponent[10, b]
  = MantissaExponent[10, b]
