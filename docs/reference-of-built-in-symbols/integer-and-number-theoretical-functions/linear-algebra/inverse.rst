Inverse
=======

`WMA link <https://reference.wolfram.com/language/ref/Inverse.html>`_


:code:`Inverse` [:math:`m`]
    computes the inverse of the matrix :math:`m`.





>>> Inverse[{{1, 2, 0}, {2, 3, 0}, {3, 4, 1}}]
    =

:math:`\left\{\left\{-3,2,0\right\},\left\{2,-1,0\right\},\left\{1,-2,1\right\}\right\}`


>>> Inverse[{{1, 0}, {0, 0}}]

    Inverse::sing The matrix {{1, 0}, {0, 0}} is singular.
    =

:math:`\text{Inverse}\left[\left\{\left\{1,0\right\},\left\{0,0\right\}\right\}\right]`


