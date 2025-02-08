MantissaExponent
================

`WMA link <https://reference.wolfram.com/language/ref/MantissaExponent.html>`_


:code:`MantissaExponent` [:math:`n`]
    finds a list containing the mantissa and exponent of a given number :math:`n`.

:code:`MantissaExponent` [:math:`n`, :math:`b`]
    finds the base b mantissa and exponent of :math:`n`.





>>> MantissaExponent[2.5*10^20]
    =

:math:`\left\{0.25,21\right\}`


>>> MantissaExponent[125.24]
    =

:math:`\left\{0.12524,3\right\}`


>>> MantissaExponent[125., 2]
    =

:math:`\left\{0.976563,7\right\}`


>>> MantissaExponent[10, b]
    =

:math:`\text{MantissaExponent}\left[10,b\right]`


