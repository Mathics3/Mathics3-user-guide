RealValuedNumberQ
=================

`WMA link <https://reference.wolfram.com/language/ref/RealValuedNumberQ.html>`_


:code:`RealValuedNumberQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is an explicit number with no imaginary component.





>>> RealValuedNumberQ[10]

    =
:math:`\text{True}`


>>> RealValuedNumberQ[4.0]

    =
:math:`\text{True}`


>>> RealValuedNumberQ[1+I]

    =
:math:`\text{False}`


>>> RealValuedNumberQ[0 * I]

    =
:math:`\text{True}`


>>> RealValuedNumberQ[0.0 * I]

    =
:math:`\text{False}`



"Underflow[]" and "Overflow[]" are considered Real valued numbers:

>>> {RealValuedNumberQ[Underflow[]], RealValuedNumberQ[Overflow[]]}

    =
:math:`\left\{\text{True},\text{True}\right\}`


