OwnValues
=========

`WMA link <https://reference.wolfram.com/language/ref/OwnValues.html>`_

:code:`OwnValues` [:math:`symbol`]
    gives the list of ownvalue associated with :math:`symbol`.





>>> x = 3;


>>> x = 2;


>>> OwnValues[x]
    =

:math:`\left\{\text{HoldPattern}\left[x\right]\text{:>}2\right\}`


>>> x := y


>>> OwnValues[x]
    =

:math:`\left\{\text{HoldPattern}\left[x\right]\text{:>}y\right\}`


>>> y = 5;


>>> OwnValues[x]
    =

:math:`\left\{\text{HoldPattern}\left[x\right]\text{:>}y\right\}`


>>> Hold[x] /. OwnValues[x]
    =

:math:`\text{Hold}\left[y\right]`


>>> Hold[x] /. OwnValues[x] // ReleaseHold
    =

:math:`5`


