CoefficientList
===============

`WMA link <https://reference.wolfram.com/language/ref/CoefficientList.html>`_


:code:`CoefficientList[poly, var]`
    returns a list of coefficients of powers of :math:`var` in :math:`poly`, starting with power 0.

:code:`CoefficientList[poly, {var1, var2, ...}]`
    returns an array of coefficients of the :math:`vari`.





>>> CoefficientList[(x + 3)^5, x]
  = {243, 405, 270, 90, 15, 1}
>>> CoefficientList[(x + y)^4, x]
  = {y ^ 4, 4 y ^ 3, 6 y ^ 2, 4 y, 1}
>>> CoefficientList[a x^2 + b y^3 + c x + d y + 5, x]
  = {5 + b y ^ 3 + d y, c, a}
>>> CoefficientList[(x + 2)/(y - 3) + x/(y - 2), x]
  = {2 / (-3 + y), 1 / (-3 + y) + 1 / (-2 + y)}
>>> CoefficientList[(x + y)^3, z]
  = {(x + y) ^ 3}
>>> CoefficientList[a x^2 + b y^3 + c x + d y + 5, {x, y}]
  = {{5, d, 0, b}, {c, 0, 0, 0}, {a, 0, 0, 0}}
>>> CoefficientList[(x - 2 y + 3 z)^3, {x, y, z}]
  = {{{0, 0, 0, 27}, {0, 0, -54, 0}, {0, 36, 0, 0}, {-8, 0, 0, 0}}, {{0, 0, 27, 0}, {0, -36, 0, 0}, {12, 0, 0, 0}, {0, 0, 0, 0}}, {{0, 9, 0, 0}, {-6, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}}, {{1, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}}}
>>> CoefficientList[Series[Log[1-x], {x, 0, 9}], x]
  = {0, -1, -1 / 2, -1 / 3, -1 / 4, -1 / 5, -1 / 6, -1 / 7, -1 / 8, -1 / 9}
>>> CoefficientList[Series[2x, {x, 0, 9}], x]
  = {0, 2}
