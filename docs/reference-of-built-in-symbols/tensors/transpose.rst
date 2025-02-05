Transpose
=========

`Transpose <https://en.wikipedia.org/wiki/Transpose>`_ (`WMA <https://reference.wolfram.com/language/ref/Transpose.html>`_)


:code:`Transpose` [:math:`m`]
    transposes rows and columns in the matrix :math:`m`.





>>> square = {{1, 2, 3}, {4, 5, 6}}; Transpose[square]
  = {{1, 4}, {2, 5}, {3, 6}}
>>> MatrixForm[%]
  = 1   4
    
    2   5
    
    3   6
>>> matrix = {{1, 2}, {3, 4}, {5, 6}}; MatrixForm[Transpose[matrix]]
  = 1   3   5
    
    2   4   6

Transpose is its own inverse. Transposing a matrix twice will give you back the same thing you started out with:

>>> Transpose[Transpose[matrix]] == matrix
  = True
>>> Clear[matrix, square]

