NHoldAll
========

`WMA link <https://reference.wolfram.com/language/ref/NHoldAll.html>`_


:code:`NHoldAll`
    is an attribute that protects all arguments of a          function from numeric evaluation.





>>> N[f[2, 3]]
    =

:math:`f\left[2.,3.\right]`


>>> SetAttributes[f, NHoldAll]


>>> N[f[2, 3]]
    =

:math:`f\left[2,3\right]`


