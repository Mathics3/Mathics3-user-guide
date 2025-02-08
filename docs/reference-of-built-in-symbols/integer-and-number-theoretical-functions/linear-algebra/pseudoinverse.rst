PseudoInverse
=============

`WMA link <https://reference.wolfram.com/language/ref/PseudoInverse.html>`_


:code:`PseudoInverse` [:math:`m`]
    computes the Moore-Penrose pseudoinverse of the matrix :math:`m`.
    If :math:`m` is invertible, the pseudoinverse equals the inverse.





>>> PseudoInverse[{{1, 2}, {2, 3}, {3, 4}}]
    =

:math:`\left\{\left\{-\frac{11}{6},-\frac{1}{3},\frac{7}{6}\right\},\left\{\frac{4}{3},\frac{1}{3},-\frac{2}{3}\right\}\right\}`


>>> PseudoInverse[{{1, 2, 0}, {2, 3, 0}, {3, 4, 1}}]
    =

:math:`\left\{\left\{-3,2,0\right\},\left\{2,-1,0\right\},\left\{1,-2,1\right\}\right\}`


>>> PseudoInverse[{{1.0, 2.5}, {2.5, 1.0}}]
    =

:math:`\left\{\left\{-0.190476,0.47619\right\},\left\{0.47619,-0.190476\right\}\right\}`


