DSolve
======

`WMA link <https://reference.wolfram.com/language/ref/DSolve.html>`_


:code:`DSolve[:math:`eq`, :math:`y`` [:math:`x`], :math:`x`]
    solves a differential equation for the function :math:`y`[:math:`x`].





>>> DSolve[y''[x] == 0, y[x], x]
  = {{y[x] -> x C[2] + C[1]}}
>>> DSolve[y''[x] == y[x], y[x], x]
  = {{y[x] -> C[1] E ^ (-x) + C[2] E ^ x}}
>>> DSolve[y''[x] == y[x], y, x]
  = {{y -> Function[{x}, C[1] E ^ (-x) + C[2] E ^ x]}}

DSolve can also solve basic PDE

>>> DSolve[D[f[x, y], x] / f[x, y] + 3 D[f[x, y], y] / f[x, y] == 2, f, {x, y}]
  = {{f -> Function[{x, y}, E ^ (x / 5 + 3 y / 5) C[1][3 x - y]]}}
>>> DSolve[D[f[x, y], x] x + D[f[x, y], y] y == 2, f[x, y], {x, y}]
  = {{f[x, y] -> 2 Log[x] + C[1][y / x]}}
>>> DSolve[D[y[x, t], t] + 2 D[y[x, t], x] == 0, y[x, t], {x, t}]
  = {{y[x, t] -> C[1][x - 2 t]}}
