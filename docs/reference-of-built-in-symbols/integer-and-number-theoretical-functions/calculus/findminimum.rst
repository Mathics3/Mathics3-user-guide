FindMinimum
===========

`WMA link <https://reference.wolfram.com/language/ref/FindMinimum.html>`_


:code:`FindMinimum` [:math:`f`, {:math:`x`, :math:`x_0`}]
    searches for a numerical minimum of :math:`f`, starting from :code:`:math:`x`=:math:`x_0`` .





:code:`FindMinimum`  by default uses Newton's method, so the function of interest should have a first derivative.

>>> FindMinimum[(x-3)^2+2., {x, 1}]
  = {2., {x -> 3.}}
>>> FindMinimum[10*^-30 *(x-3)^2+2., {x, 1}]
  = {2., {x -> 3.}}
>>> FindMinimum[Sin[x], {x, 1}]
  = {-1., {x -> -1.5708}}
>>> phi[x_?NumberQ]:=NIntegrate[u,{u,0,x}, Method->"Internal"];

>>> Quiet[FindMinimum[phi[x]-x,{x, 1.2}, Method->"Newton"]]
  = {-0.5, {x -> 1.00001}}
>>> Clear[phi];


For a not so well behaving function, the result can be less accurate:

>>> FindMinimum[Exp[-1/x^2]+1., {x,1.2}, MaxIterations->10]
  = FindMinimum[Exp[-1 / x ^ 2] + 1., {x, 1.2}, MaxIterations -> 10]
