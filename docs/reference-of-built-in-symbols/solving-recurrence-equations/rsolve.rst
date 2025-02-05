RSolve
======

`WMA link <https://reference.wolfram.com/language/ref/RSolve.html>`_


:code:`RSolve[:math:`eqn`, :math:`a`` [:math:`n`], :math:`n`]
    solves a recurrence equation for the function :code:`:math:`a`[:math:`n`]` .





Solve a difference equation:

>>> RSolve[a[n] == a[n+1], a[n], n]
  = {{a[n] -> C[0]}}

No boundary conditions gives two general parameters:

>>> RSolve[{a[n + 2] == a[n]}, a, n]
  = {{a -> Function[{n}, C[0] + C[1] (-1) ^ n]}}

Include one boundary condition:

>>> RSolve[{a[n + 2] == a[n], a[0] == 1}, a, n]
  = ...

Get a "pure function" solution for a with two boundary conditions:

>>> RSolve[{a[n + 2] == a[n], a[0] == 1, a[1] == 4}, a, n]
  = {{a -> Function[{n}, 5 / 2 - 3 (-1) ^ n / 2]}}
