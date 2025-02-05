LinearModelFit
==============

`WMA link <https://reference.wolfram.com/language/ref/LinearModelFit.html>`_


:code:`LinearModelFit` [:math:`m`, :math:`f`, :math:`x`]
    fits a linear model :math:`f` in the variables :math:`x` to the dataset :math:`m`.





>>> m = LinearModelFit[{{2, 1}, {3, 4}, {5, 3}, {7, 6}}, x, x];

>>> m["BasisFunctions"]
  = {1, x}
>>> m["BestFit"]
  = 0.186441 + 0.779661 x
>>> m["BestFitParameters"]
  = {0.186441, 0.779661}
>>> m["DesignMatrix"]
  = {{1, 2}, {1, 3}, {1, 5}, {1, 7}}
>>> m["Function"]
  = 0.186441 + 0.779661 #1&
>>> m["Response"]
  = {1, 4, 3, 6}
>>> m["FitResiduals"]
  = {-0.745763, 1.47458, -1.08475, 0.355932}
>>> m = LinearModelFit[{{2, 2, 1}, {3, 2, 4}, {5, 6, 3}, {7, 9, 6}}, {Sin[x], Cos[y]}, {x, y}];

>>> m["BasisFunctions"]
  = {1, Sin[x], Cos[y]}
>>> m["Function"]
  = 3.33077 - 5.65221 Cos[#2] - 5.01042 Sin[#1]&
>>> m = LinearModelFit[{{{1, 4}, {1, 5}, {1, 7}}, {1, 2, 3}}];

>>> m["BasisFunctions"]
  = {#1, #2}
>>> m["FitResiduals"]
  = {-0.142857, 0.214286, -0.0714286}
