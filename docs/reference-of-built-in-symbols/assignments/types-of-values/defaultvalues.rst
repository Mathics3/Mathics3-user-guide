DefaultValues
=============

`WMA link <https://reference.wolfram.com/language/ref/DefaultValues.html>`_


:code:`DefaultValues` [:math:`symbol`]
    gives the list of default values associated with :math:`symbol`.
    
    *Note: this function is in Mathematica 5 but has been removed from       current Mathematica.*





>>> Default[f, 1] = 4

    =
:math:`4`


>>> DefaultValues[f]

    =
:math:`\left\{\text{HoldPattern}\left[\text{Default}\left[f,1\right]\right]\text{:>}4\right\}`



You can assign values to :code:`DefaultValues` :

>>> DefaultValues[g] = {Default[g] -> 3};


>>> Default[g, 1]

    =
:math:`3`


>>> g[x_.] := {x}


>>> g[a]

    =
:math:`\left\{a\right\}`


>>> g[]

    =
:math:`\left\{3\right\}`


