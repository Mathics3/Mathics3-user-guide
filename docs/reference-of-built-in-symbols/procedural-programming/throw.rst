Throw
=====

`WMA link <https://reference.wolfram.com/language/ref/Throw.html>`_


:code:`Throw[`value`]`
    stops evaluation and returns `value` as the value of the nearest            enclosing :code:`Catch` .

:code:`Catch[`value`, `tag`]`
    is caught only by `Catch[expr,form]`, where tag matches form.





Using Throw can affect the structure of what is returned by a function:

>>> NestList[#^2 + 1 &, 1, 7]

    =
:math:`\left\{1,2,5,26,677,458330,210066388901,44127887745906175987802\right\}`


>>> Catch[NestList[If[# > 1000, Throw[#], #^2 + 1] &, 1, 7]]

    =
:math:`458330`


>>> Throw[1]

    Throw::nocatch Uncaught Throw[1] returned to top level.

    =
:math:`\text{Hold}\left[\text{Throw}\left[1\right]\right]`


