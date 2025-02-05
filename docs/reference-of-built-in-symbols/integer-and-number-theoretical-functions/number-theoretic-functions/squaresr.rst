SquaresR
========

`Sum of squares function <https://en.wikipedia.org/wiki/Sum_of_squares_function>`_ (`WMA <https://reference.wolfram.com/language/ref/SquaresR.html>`_)


:code:`SquaresR` [:math:`d`, :math:`n`]
    returns the number of ways to represent :math:`n` as a sum of :math:`d` squares.





>>> Table[SquaresR[2, n], {n, 10}]
  = {4, 4, 0, 4, 8, 0, 0, 4, 4, 8}
>>> Table[Sum[SquaresR[2, k], {k, 0, n^2}], {n, 5}]
  = {5, 13, 29, 49, 81}
>>> Table[SquaresR[4, n], {n, 10}]
  = {8, 24, 32, 24, 48, 96, 64, 24, 104, 144}
>>> Table[SquaresR[6, n], {n, 10}]
  = {12, 60, 160, 252, 312, 544, 960, 1020, 876, 1560}
>>> Table[SquaresR[8, n], {n, 10}]
  = {16, 112, 448, 1136, 2016, 3136, 5504, 9328, 12112, 14112}
