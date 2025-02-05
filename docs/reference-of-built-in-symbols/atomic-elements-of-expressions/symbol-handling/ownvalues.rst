OwnValues
=========

`WMA link <https://reference.wolfram.com/language/ref/OwnValues.html>`_

:code:`OwnValues` [:math:`symbol`]
    gives the list of ownvalue associated with :math:`symbol`.





>>> x = 3;

>>> x = 2;

>>> OwnValues[x]
  = {HoldPattern[x] :> 2}
>>> x := y

>>> OwnValues[x]
  = {HoldPattern[x] :> y}
>>> y = 5;

>>> OwnValues[x]
  = {HoldPattern[x] :> y}
>>> Hold[x] /. OwnValues[x]
  = Hold[y]
>>> Hold[x] /. OwnValues[x] // ReleaseHold
  = 5
