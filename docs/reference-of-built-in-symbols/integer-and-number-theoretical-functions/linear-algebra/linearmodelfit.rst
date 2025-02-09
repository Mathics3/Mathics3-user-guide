LinearModelFit
==============

`WMA link <https://reference.wolfram.com/language/ref/LinearModelFit.html>`_


:code:`LinearModelFit` [:math:`m`, :math:`f`, :math:`x`]
    fits a linear model :math:`f` in the variables :math:`x` to the dataset :math:`m`.





>>> m = LinearModelFit[{{2, 1}, {3, 4}, {5, 3}, {7, 6}}, x, x];


>>> m["BasisFunctions"]

    =
:math:`\left\{1,x\right\}`


>>> m["BestFit"]

    =
:math:`0.186441+0.779661 x`


>>> m["BestFitParameters"]

    =
:math:`\left\{0.186441,0.779661\right\}`


>>> m["DesignMatrix"]

    =
:math:`\left\{\left\{1,2\right\},\left\{1,3\right\},\left\{1,5\right\},\left\{1,7\right\}\right\}`


>>> m["Function"]

    =
:math:`0.186441+0.779661 \text{\#1}\&`


>>> m["Response"]

    =
:math:`\left\{1,4,3,6\right\}`


>>> m["FitResiduals"]

    =
:math:`\left\{-0.745763,1.47458,-1.08475,0.355932\right\}`


>>> m = LinearModelFit[{{2, 2, 1}, {3, 2, 4}, {5, 6, 3}, {7, 9, 6}}, {Sin[x], Cos[y]}, {x, y}];


>>> m["BasisFunctions"]

    =
:math:`\left\{1,\text{Sin}\left[x\right],\text{Cos}\left[y\right]\right\}`


>>> m["Function"]

    =
:math:`3.33077-5.65221 \text{Cos}\left[\text{\#2}\right]-5.01042 \text{Sin}\left[\text{\#1}\right]\&`


>>> m = LinearModelFit[{{{1, 4}, {1, 5}, {1, 7}}, {1, 2, 3}}];


>>> m["BasisFunctions"]

    =
:math:`\left\{\text{\#1},\text{\#2}\right\}`


>>> m["FitResiduals"]

    =
:math:`\left\{-0.142857,0.214286,-0.0714286\right\}`


