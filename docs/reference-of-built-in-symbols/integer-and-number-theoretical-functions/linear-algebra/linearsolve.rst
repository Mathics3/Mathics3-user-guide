LinearSolve
===========

`WMA link <https://reference.wolfram.com/language/ref/LinearSolve.html>`_


:code:`LinearSolve` [:math:`matrix`, :math:`right`]
    solves the linear equation system :code:`:math:`matrix` . :math:`x` = :math:`right``
    and returns one corresponding solution :math:`x`.





>>> LinearSolve[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}, {1, 2, 3}]

    =
:math:`\left\{0,1,2\right\}`



Test the solution:

>>> {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}} . {0, 1, 2}

    =
:math:`\left\{1,2,3\right\}`



If there are several solutions, one arbitrary solution is returned:

>>> LinearSolve[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {1, 1, 1}]

    =
:math:`\left\{-1,1,0\right\}`



Infeasible systems are reported:

>>> LinearSolve[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {1, -2, 3}]

    LinearSolve::nosol Linear equation encountered that has no solution.

    =
:math:`\text{LinearSolve}\left[\left\{\left\{1,2,3\right\},\left\{4,5,6\right\},\left\{7,8,9\right\}\right\},\left\{1,-2,3\right\}\right]`


