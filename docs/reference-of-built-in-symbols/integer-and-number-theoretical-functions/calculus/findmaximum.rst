FindMaximum
===========

`WMA link <https://reference.wolfram.com/language/ref/FindMaximum.html>`_


:code:`FindMaximum` [:math:`f`, {:math:`x`, :math:`x_0`}]
    searches for a numerical maximum of :math:`f`, starting from :code:`:math:`x`=:math:`x_0`` .





:code:`FindMaximum`  by default uses Newton's method, so the function of interest should have a first derivative.

>>> FindMaximum[-(x-3)^2+2., {x, 1}]
  = {2., {x -> 3.}}
>>> FindMaximum[-10*^-30 *(x-3)^2+2., {x, 1}]
  = {2., {x -> 3.}}
>>> FindMaximum[Sin[x], {x, 1}]
  = {1., {x -> 1.5708}}
>>> phi[x_?NumberQ]:=NIntegrate[u, {u, 0., x}, Method->"Internal"];

>>> Quiet[FindMaximum[-phi[x] + x, {x, 1.2}, Method->"Newton"]]
  = {0.5, {x -> 1.00001}}
>>> Clear[phi];


For a not so well behaving function, the result can be less accurate:

>>> FindMaximum[-Exp[-1/x^2]+1., {x,1.2}, MaxIterations->10]
  = FindMaximum[-Exp[-1 / x ^ 2] + 1., {x, 1.2}, MaxIterations -> 10]
