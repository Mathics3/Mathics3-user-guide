FormatValues
============

`WMA link <https://reference.wolfram.com/language/tutorial/PatternsAndTransformationRules.html#6025>`_

:code:`FormatValues` [:math:`symbol`]
    gives the list of formatvalues associated with :math:`symbol`.





>>> Format[F[x_], OutputForm]:= Subscript[x, F]


>>> FormatValues[F]
    =

:math:`\left\{\text{HoldPattern}\left[\text{Format}\left[F\left[\text{x\_}\right],\text{OutputForm}\right]\right]\text{:>}x_F\right\}`


