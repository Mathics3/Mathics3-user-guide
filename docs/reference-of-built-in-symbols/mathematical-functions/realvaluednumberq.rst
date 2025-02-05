RealValuedNumberQ
=================

`WMA link <https://reference.wolfram.com/language/ref/RealValuedNumberQ.html>`_


:code:`RealValuedNumberQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is an explicit number with no imaginary component.





>>> RealValuedNumberQ[10]
  = True
>>> RealValuedNumberQ[4.0]
  = True
>>> RealValuedNumberQ[1+I]
  = False
>>> RealValuedNumberQ[0 * I]
  = True
>>> RealValuedNumberQ[0.0 * I]
  = False

"Underflow[]" and "Overflow[]" are considered Real valued numbers:

>>> {RealValuedNumberQ[Underflow[]], RealValuedNumberQ[Overflow[]]}
  = {True, True}
