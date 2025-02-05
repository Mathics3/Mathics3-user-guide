PseudoInverse
=============

`WMA link <https://reference.wolfram.com/language/ref/PseudoInverse.html>`_


:code:`PseudoInverse` [:math:`m`]
    computes the Moore-Penrose pseudoinverse of the matrix :math:`m`.
    If :math:`m` is invertible, the pseudoinverse equals the inverse.





>>> PseudoInverse[{{1, 2}, {2, 3}, {3, 4}}]
  = {{-11 / 6, -1 / 3, 7 / 6}, {4 / 3, 1 / 3, -2 / 3}}
>>> PseudoInverse[{{1, 2, 0}, {2, 3, 0}, {3, 4, 1}}]
  = {{-3, 2, 0}, {2, -1, 0}, {1, -2, 1}}
>>> PseudoInverse[{{1.0, 2.5}, {2.5, 1.0}}]
  = {{-0.190476, 0.47619}, {0.47619, -0.190476}}
