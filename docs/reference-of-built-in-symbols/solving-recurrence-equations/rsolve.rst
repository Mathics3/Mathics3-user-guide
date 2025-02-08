RSolve
======

`WMA link <https://reference.wolfram.com/language/ref/RSolve.html>`_


:code:`RSolve[:math:`eqn`, :math:`a`` [:math:`n`], :math:`n`]
    solves a recurrence equation for the function :code:`:math:`a`[:math:`n`]` .





Solve a difference equation:

>>> RSolve[a[n] == a[n+1], a[n], n]
    =

:math:`\left\{\left\{a\left[n\right]->C\left[0\right]\right\}\right\}`



No boundary conditions gives two general parameters:

>>> RSolve[{a[n + 2] == a[n]}, a, n]
    =

:math:`\left\{\left\{a->\text{Function}\left[\left\{n\right\},C\left[0\right]+C\left[1\right] \left(-1\right){}^{\wedge}n\right]\right\}\right\}`



Include one boundary condition:

>>> RSolve[{a[n + 2] == a[n], a[0] == 1}, a, n]
    =

:math:`\left\{\left\{a->\text{Function}\left[\left\{n\right\},1-C\left[1\right]+C\left[1\right] \left(-1\right){}^{\wedge}n\right]\right\}\right\}`



Get a "pure function" solution for a with two boundary conditions:

>>> RSolve[{a[n + 2] == a[n], a[0] == 1, a[1] == 4}, a, n]
    =

:math:`\left\{\left\{a->\text{Function}\left[\left\{n\right\},\frac{5}{2}-\frac{3 \left(-1\right){}^{\wedge}n}{2}\right]\right\}\right\}`


