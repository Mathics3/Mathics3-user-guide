FindMaximum
===========

`WMA link <https://reference.wolfram.com/language/ref/FindMaximum.html>`_


:code:`FindMaximum` [:math:`f`, {:math:`x`, :math:`x_0`}]
    searches for a numerical maximum of :math:`f`, starting from :code:`:math:`x`=:math:`x_0`` .





:code:`FindMaximum`  by default uses Newton's method, so the function of interest should have a first derivative.

>>> FindMaximum[-(x-3)^2+2., {x, 1}]

    FindMaximum::fmgz Encountered a gradient that is effectively zero. The result returned may not be a maximum; it may be a minimum or a saddle point.

    =
:math:`\left\{2.,\left\{x->3.\right\}\right\}`


>>> FindMaximum[-10*^-30 *(x-3)^2+2., {x, 1}]

    FindMaximum::fmgz Encountered a gradient that is effectively zero. The result returned may not be a maximum; it may be a minimum or a saddle point.

    =
:math:`\left\{2.,\left\{x->3.\right\}\right\}`


>>> FindMaximum[Sin[x], {x, 1}]

    =
:math:`\left\{1.,\left\{x->1.5708\right\}\right\}`


>>> phi[x_?NumberQ]:=NIntegrate[u, {u, 0., x}, Method->"Internal"];


>>> Quiet[FindMaximum[-phi[x] + x, {x, 1.2}, Method->"Newton"]]

    =
:math:`\left\{0.5,\left\{x->1.00001\right\}\right\}`


>>> Clear[phi];



For a not so well behaving function, the result can be less accurate:

>>> FindMaximum[-Exp[-1/x^2]+1., {x,1.2}, MaxIterations->10]

    FindMaximum::maxiter The maximum number of iterations was exceeded. The result might be inaccurate.

    =
:math:`\text{FindMaximum}\left[-\text{Exp}\left[-\frac{1}{x^2}\right]+1.,\left\{x,1.2\right\},\text{MaxIterations}->10\right]`


