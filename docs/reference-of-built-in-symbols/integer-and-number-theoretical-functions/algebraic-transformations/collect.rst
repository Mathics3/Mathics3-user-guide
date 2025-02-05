Collect
=======

`WMA link <https://reference.wolfram.com/language/ref/Collect.html>`_


:code:`Collect` [:math:`expr`, :math:`x`]
    Expands :math:`expr` and collect together terms having the same power of :math:`x`.

:code:`Collect` [:math:`expr`, {:math:`x_1`, :math:`x_2`, ...}]
    Expands :math:`expr` and collect together terms having the same powers of          :math:`x_1`, :math:`x_2`, ....

:code:`Collect` [:math:`expr`, {:math:`x_1`, :math:`x_2`, ...}, :math:`filter`]
    After collect the terms, applies :math:`filter` to each coefficient.





>>> Collect[(x+y)^3, y]
  = x ^ 3 + 3 x ^ 2 y + 3 x y ^ 2 + y ^ 3
>>> Collect[2 Sin[x z] (x+2 y^2 + Sin[y] x), y]
  = 2 x Sin[x z] + 2 x Sin[x z] Sin[y] + 4 y ^ 2 Sin[x z]
>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, y]
  = 4 x Sin[x z] + x ^ 3 + y (3 x + 3 x ^ 2) + y ^ 2 (3 x + 4 Sin[x z]) + y ^ 3
>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, {x,y}]
  = 4 x Sin[x z] + x ^ 3 + 3 x y + 3 x ^ 2 y + 4 y ^ 2 Sin[x z] + 3 x y ^ 2 + y ^ 3
>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, {x,y}, h]
  = x h[4 Sin[x z]] + x ^ 3 h[1] + x y h[3] + x ^ 2 y h[3] + y ^ 2 h[4 Sin[x z]] + x y ^ 2 h[3] + y ^ 3 h[1]
