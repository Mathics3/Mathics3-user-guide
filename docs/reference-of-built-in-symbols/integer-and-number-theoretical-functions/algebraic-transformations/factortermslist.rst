FactorTermsList
===============

`WMA link <https://reference.wolfram.com/language/ref/FactorTermsList.html>`_


:code:`FactorTermsList[poly]`
    returns a list of 2 elements.
    The first element is the numerical factor in :math:`poly`.
    The second one is the remaining of the polynomial with numerical factor removed.

:code:`FactorTermsList[poly, {x1, x2, ...}]`
    returns a list of factors in :math:`poly`.
    The first element is the numerical factor in :math:`poly`.         The next ones are factors that are independent of variables lists which         are created by removing each variable :math:`xi` from right to left.         The last one is the remaining of polynomial after dividing :math:`poly` to all previous factors.





>>> FactorTermsList[2 x^2 - 2]
    =

:math:`\left\{2,-1+x^2\right\}`


>>> FactorTermsList[x^2 - 2 x + 1]
    =

:math:`\left\{1,1-2 x+x^2\right\}`


>>> f = 3 (-1 + 2 x) (-1 + y) (1 - a)
    =

:math:`3 \left(-1+2 x\right) \left(-1+y\right) \left(1-a\right)`


>>> FactorTermsList[f]
    =

:math:`\left\{-3,-1+a-2 a x-a y+2 x+y-2 x y+2 a x y\right\}`


>>> FactorTermsList[f, x]
    =

:math:`\left\{-3,1-a-y+a y,-1+2 x\right\}`


