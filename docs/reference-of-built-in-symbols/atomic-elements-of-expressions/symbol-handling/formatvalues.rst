FormatValues
============

`WMA link <https://reference.wolfram.com/language/tutorial/PatternsAndTransformationRules.html#6025>`_

:code:`FormatValues` [:math:`symbol`]
    gives the list of formatvalues associated with :math:`symbol`.





>>> Format[F[x_], OutputForm]:= Subscript[x, F]

>>> FormatValues[F]
  = {HoldPattern[Format[Subscript[x_, F], OutputForm]] :> Subscript[x, F]}
