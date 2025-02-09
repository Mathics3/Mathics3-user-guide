Return
======

`WMA link <https://reference.wolfram.com/language/ref/Return.html>`_


:code:`Return` [:math:`expr`]
    aborts a function call and returns :math:`expr`.





>>> f[x_] := (If[x < 0, Return[0]]; x)


>>> f[-1]

    =
:math:`0`


>>> Clear[f]
    = `

>>> Do[If[i > 3, Return[]]; Print[i], {i, 10}]

    1

    2

    3



:code:`Return`  only exits from the innermost control flow construct.

>>> g[x_] := (Do[If[x < 0, Return[0]], {i, {2, 1, 0, -1}}]; x)


>>> g[-1]

    =
:math:`-1`


