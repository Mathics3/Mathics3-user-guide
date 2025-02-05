SubValues
=========

`WMA link <https://reference.wolfram.com/language/ref/SubValues.html>`_


:code:`SubValues` [:math:`symbol`]
    gives the list of subvalues associated with :math:`symbol`.
    
    *Note: this function is not in current Mathematica.*





>>> f[1][x_] := x

>>> f[2][x_] := x ^ 2

>>> SubValues[f]
  = {HoldPattern[f[2][x_]] :> x ^ 2, HoldPattern[f[1][x_]] :> x}
>>> Definition[f]
  = f[2][x_] = x ^ 2
    
    f[1][x_] = x
