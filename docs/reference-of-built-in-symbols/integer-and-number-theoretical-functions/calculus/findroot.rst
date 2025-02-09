FindRoot
========

`WMA link <https://reference.wolfram.com/language/ref/FindRoot.html>`_


:code:`FindRoot` [:math:`f`, {:math:`x`, :math:`x_0`}]
    searches for a numerical root of :math:`f`, starting from :code:`:math:`x`=:math:`x_0`` .

:code:`FindRoot` [:math:`lhs` == :math:`rhs`, {:math:`x`, :math:`x_0`}]
    tries to solve the equation :code:`:math:`lhs` == :math:`rhs`` .





:code:`FindRoot`  by default uses Newton's method, so the function of interest should have a first derivative.

>>> FindRoot[Cos[x], {x, 1}]

    =
:math:`\left\{x->1.5708\right\}`


>>> FindRoot[Sin[x] + Exp[x],{x, 0}]

    =
:math:`\left\{x->-0.588533\right\}`


>>> FindRoot[Sin[x] + Exp[x] == Pi,{x, 0}]

    =
:math:`\left\{x->0.866815\right\}`



:code:`FindRoot`  has attribute :code:`HoldAll`  and effectively uses :code:`Block`  to localize :math:`x`.
However, in the result :math:`x` will eventually still be replaced by its value.

>>> x = "I am the result!";


>>> FindRoot[Tan[x] + Sin[x] == Pi, {x, 1}]

    =
:math:`\left\{\text{I am the result!}->1.14911\right\}`


>>> Clear[x]



:code:`FindRoot`  stops after 100 iterations:

>>> FindRoot[x^2 + x + 1, {x, 1}]

    FindRoot::maxiter The maximum number of iterations was exceeded. The result might be inaccurate.

    =
:math:`\left\{x->-1.\right\}`



Find complex roots:

>>> FindRoot[x ^ 2 + x + 1, {x, -I}]

    =
:math:`\left\{x->-0.5-0.866025 I\right\}`



The function has to return numerical values:

>>> FindRoot[f[x] == 0, {x, 0}]

    FindRoot::nnum The function value is not a number at x = 0..

    =
:math:`\text{FindRoot}\left[f\left[x\right]-0,\left\{x,0\right\}\right]`



The derivative must not be 0:

>>> FindRoot[Sin[x] == x, {x, 0}]

    FindRoot::dsing Encountered a singular derivative at the point x = 0..

    =
:math:`\text{FindRoot}\left[\text{Sin}\left[x\right]-x,\left\{x,0\right\}\right]`


>>> FindRoot[x^2 - 2, {x, 1,3}, Method->"Secant"]

    =
:math:`\left\{x->1.41421\right\}`


