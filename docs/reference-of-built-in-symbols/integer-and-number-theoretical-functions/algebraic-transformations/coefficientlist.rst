CoefficientList
===============

`WMA link <https://reference.wolfram.com/language/ref/CoefficientList.html>`_


:code:`CoefficientList[poly, var]`
    returns a list of coefficients of powers of :math:`var` in :math:`poly`, starting with power 0.

:code:`CoefficientList[poly, {var1, var2, ...}]`
    returns an array of coefficients of the :math:`vari`.





>>> CoefficientList[(x + 3)^5, x]

    =
:math:`\left\{243,405,270,90,15,1\right\}`


>>> CoefficientList[(x + y)^4, x]

    =
:math:`\left\{y^4,4 y^3,6 y^2,4 y,1\right\}`


>>> CoefficientList[a x^2 + b y^3 + c x + d y + 5, x]

    =
:math:`\left\{5+b y^3+d y,c,a\right\}`


>>> CoefficientList[(x + 2)/(y - 3) + x/(y - 2), x]

    =
:math:`\left\{\frac{2}{-3+y},\frac{1}{-3+y}+\frac{1}{-2+y}\right\}`


>>> CoefficientList[(x + y)^3, z]

    =
:math:`\left\{\left(x+y\right)^3\right\}`


>>> CoefficientList[a x^2 + b y^3 + c x + d y + 5, {x, y}]

    =
:math:`\left\{\left\{5,d,0,b\right\},\left\{c,0,0,0\right\},\left\{a,0,0,0\right\}\right\}`


>>> CoefficientList[(x - 2 y + 3 z)^3, {x, y, z}]

    =
:math:`\left\{\left\{\left\{0,0,0,27\right\},\left\{0,0,-54,0\right\},\left\{0,36,0,0\right\},\left\{-8,0,0,0\right\}\right\},\left\{\left\{0,0,27,0\right\},\left\{0,-36,0,0\right\},\left\{12,0,0,0\right\},\left\{0,0,0,0\right\}\right\},\left\{\left\{0,9,0,0\right\},\left\{-6,0,0,0\right\},\left\{0,0,0,0\right\},\left\{0,0,0,0\right\}\right\},\left\{\left\{1,0,0,0\right\},\left\{0,0,0,0\right\},\left\{0,0,0,0\right\},\left\{0,0,0,0\right\}\right\}\right\}`


>>> CoefficientList[Series[Log[1-x], {x, 0, 9}], x]

    =
:math:`\left\{0,-1,-\frac{1}{2},-\frac{1}{3},-\frac{1}{4},-\frac{1}{5},-\frac{1}{6},-\frac{1}{7},-\frac{1}{8},-\frac{1}{9}\right\}`


>>> CoefficientList[Series[2x, {x, 0, 9}], x]

    =
:math:`\left\{0,2\right\}`


