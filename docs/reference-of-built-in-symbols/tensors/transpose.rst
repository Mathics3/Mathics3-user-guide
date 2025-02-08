Transpose
=========

`Transpose <https://en.wikipedia.org/wiki/Transpose>`_ (`WMA <https://reference.wolfram.com/language/ref/Transpose.html>`_)


:code:`Transpose` [:math:`m`]
    transposes rows and columns in the matrix :math:`m`.





>>> square = {{1, 2, 3}, {4, 5, 6}}; Transpose[square]
    =

:math:`\left\{\left\{1,4\right\},\left\{2,5\right\},\left\{3,6\right\}\right\}`


>>> MatrixForm[%]
    =

:math:`\left(\begin{array}{cc} 1 & 4\\ 2 & 5\\ 3 & 6\end{array}\right)`


>>> matrix = {{1, 2}, {3, 4}, {5, 6}}; MatrixForm[Transpose[matrix]]
    =

:math:`\left(\begin{array}{ccc} 1 & 3 & 5\\ 2 & 4 & 6\end{array}\right)`



Transpose is its own inverse. Transposing a matrix twice will give you back the same thing you started out with:

>>> Transpose[Transpose[matrix]] == matrix
    =

:math:`\text{True}`


>>> Clear[matrix, square]
    = `

