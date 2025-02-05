UpValues
========

`WMA link <https://reference.wolfram.com/language/ref/UpValues.html>`_

:code:`UpValues` [:math:`symbol`]
    gives the list of transformation rules corresponding to upvalues           define with :math:`symbol`.





>>> a + b ^= 2
  = 2
>>> UpValues[a]
  = {HoldPattern[a + b] :> 2}
>>> UpValues[b]
  = {HoldPattern[a + b] :> 2}

You can assign values to :code:`UpValues` :

>>> UpValues[pi] := {Sin[pi] :> 0}

>>> Sin[pi]
  = 0
