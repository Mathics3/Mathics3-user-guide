CoefficientArrays
=================

`WMA link <https://reference.wolfram.com/language/ref/CoefficientArrays.html>`_


:code:`CoefficientArrays` [:math:`polys`, :math:`vars`]
    returns a list of arrays of coefficients of the variables :math:`vars`           in the polynomial  :math:`poly`.





>>> CoefficientArrays[1 + x^3, x]
  = {1, {0}, {{0}}, {{{1}}}}
>>> CoefficientArrays[1 + x y+ x^3, {x, y}]
  = {1, {0, 0}, {{0, 1}, {0, 0}}, {{{1, 0}, {0, 0}}, {{0, 0}, {0, 0}}}}
>>> CoefficientArrays[{1 + x^2, x y}, {x, y}]
  = {{1, 0}, {{0, 0}, {0, 0}}, {{{1, 0}, {0, 0}}, {{0, 1}, {0, 0}}}}
>>> CoefficientArrays[(x+y+Sin[z])^3, {x,y}]
  = {Sin[z] ^ 3, {3 Sin[z] ^ 2, 3 Sin[z] ^ 2}, {{3 Sin[z], 6 Sin[z]}, {0, 3 Sin[z]}}, {{{1, 3}, {0, 3}}, {{0, 0}, {0, 1}}}}
>>> CoefficientArrays[(x + y + Sin[z])^3, {x, z}]
  = CoefficientArrays[(x + y + Sin[z]) ^ 3, {x, z}]
