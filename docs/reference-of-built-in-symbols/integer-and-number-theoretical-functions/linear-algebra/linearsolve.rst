LinearSolve
===========

`WMA link <https://reference.wolfram.com/language/ref/LinearSolve.html>`_


:code:`LinearSolve` [:math:`matrix`, :math:`right`]
    solves the linear equation system :code:`:math:`matrix` . :math:`x` = :math:`right``
    and returns one corresponding solution :math:`x`.





>>> LinearSolve[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}, {1, 2, 3}]
  = {0, 1, 2}

Test the solution:

>>> {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}} . {0, 1, 2}
  = {1, 2, 3}

If there are several solutions, one arbitrary solution is returned:

>>> LinearSolve[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {1, 1, 1}]
  = {-1, 1, 0}

Infeasible systems are reported:

>>> LinearSolve[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {1, -2, 3}]
  = LinearSolve[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {1, -2, 3}]
