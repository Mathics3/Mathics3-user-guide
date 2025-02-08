UpValues
========

`WMA link <https://reference.wolfram.com/language/ref/UpValues.html>`_

:code:`UpValues` [:math:`symbol`]
    gives the list of transformation rules corresponding to upvalues           define with :math:`symbol`.





>>> a + b ^= 2
    =

:math:`2`


>>> UpValues[a]
    =

:math:`\left\{\text{HoldPattern}\left[a+b\right]\text{:>}2\right\}`


>>> UpValues[b]
    =

:math:`\left\{\text{HoldPattern}\left[a+b\right]\text{:>}2\right\}`



You can assign values to :code:`UpValues` :

>>> UpValues[pi] := {Sin[pi] :> 0}


>>> Sin[pi]
    =

:math:`0`


