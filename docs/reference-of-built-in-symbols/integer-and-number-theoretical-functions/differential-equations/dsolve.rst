DSolve
======

`WMA link <https://reference.wolfram.com/language/ref/DSolve.html>`_


:code:`DSolve[:math:`eq`, :math:`y`` [:math:`x`], :math:`x`]
    solves a differential equation for the function :math:`y`[:math:`x`].





>>> DSolve[y''[x] == 0, y[x], x]
    =

:math:`\left\{\left\{y\left[x\right]->x C\left[2\right]+C\left[1\right]\right\}\right\}`


>>> DSolve[y''[x] == y[x], y[x], x]
    =

:math:`\left\{\left\{y\left[x\right]->C\left[1\right] E^{-x}+C\left[2\right] E^x\right\}\right\}`


>>> DSolve[y''[x] == y[x], y, x]
    =

:math:`\left\{\left\{y->\text{Function}\left[\left\{x\right\},C\left[1\right] E^{-x}+C\left[2\right] E^x\right]\right\}\right\}`



DSolve can also solve basic PDE

>>> DSolve[D[f[x, y], x] / f[x, y] + 3 D[f[x, y], y] / f[x, y] == 2, f, {x, y}]
    =

:math:`\left\{\left\{f->\text{Function}\left[\left\{x,y\right\},E^{\frac{x}{5}+\frac{3 y}{5}} C\left[1\right]\left[3 x-y\right]\right]\right\}\right\}`


>>> DSolve[D[f[x, y], x] x + D[f[x, y], y] y == 2, f[x, y], {x, y}]
    =

:math:`\left\{\left\{f\left[x,y\right]->2 \text{Log}\left[x\right]+C\left[1\right]\left[\frac{y}{x}\right]\right\}\right\}`


>>> DSolve[D[y[x, t], t] + 2 D[y[x, t], x] == 0, y[x, t], {x, t}]
    =

:math:`\left\{\left\{y\left[x,t\right]->C\left[1\right]\left[x-2 t\right]\right\}\right\}`


