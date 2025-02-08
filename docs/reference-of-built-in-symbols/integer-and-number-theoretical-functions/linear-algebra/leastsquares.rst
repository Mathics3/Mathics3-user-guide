LeastSquares
============

`WMA link <https://reference.wolfram.com/language/ref/LeastSquares.html>`_


:code:`LeastSquares` [:math:`m`, :math:`b`]
    computes the least squares solution to :math:`m` :math:`x` = :math:`b`, finding
    an :math:`x` that solves for :math:`b` optimally.





>>> LeastSquares[{{1, 2}, {2, 3}, {5, 6}}, {1, 5, 3}]
    =

:math:`\left\{-\frac{28}{13},\frac{31}{13}\right\}`


>>> Simplify[LeastSquares[{{1, 2}, {2, 3}, {5, 6}}, {1, x, 3}]]
    =

:math:`\left\{\frac{12}{13}-\frac{8 x}{13},-\frac{4}{13}+\frac{7 x}{13}\right\}`


>>> LeastSquares[{{1, 1, 1}, {1, 1, 2}}, {1, 3}]

    LeastSquares::underdetermined Solving for underdetermined system not implemented.
    =

:math:`\text{LeastSquares}\left[\left\{\left\{1,1,1\right\},\left\{1,1,2\right\}\right\},\left\{1,3\right\}\right]`


