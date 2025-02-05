LeastSquares
============

`WMA link <https://reference.wolfram.com/language/ref/LeastSquares.html>`_


:code:`LeastSquares` [:math:`m`, :math:`b`]
    computes the least squares solution to :math:`m` :math:`x` = :math:`b`, finding
    an :math:`x` that solves for :math:`b` optimally.





>>> LeastSquares[{{1, 2}, {2, 3}, {5, 6}}, {1, 5, 3}]
  = {-28 / 13, 31 / 13}
>>> Simplify[LeastSquares[{{1, 2}, {2, 3}, {5, 6}}, {1, x, 3}]]
  = {12 / 13 - 8 x / 13, -4 / 13 + 7 x / 13}
>>> LeastSquares[{{1, 1, 1}, {1, 1, 2}}, {1, 3}]
  = LeastSquares[{{1, 1, 1}, {1, 1, 2}}, {1, 3}]
