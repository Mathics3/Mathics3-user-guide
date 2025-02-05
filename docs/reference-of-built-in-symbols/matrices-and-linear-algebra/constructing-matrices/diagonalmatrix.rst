DiagonalMatrix
==============

`WMA link <https://reference.wolfram.com/language/ref/DiagonalMatrix.html>`_


:code:`DiagonalMatrix` [:math:`list`]
    gives a matrix with the values in :math:`list` on its diagonal and       zeroes elsewhere.





>>> DiagonalMatrix[{1, 2, 3}]
  = {{1, 0, 0}, {0, 2, 0}, {0, 0, 3}}
>>> MatrixForm[%]
  = 1   0   0
    
    0   2   0
    
    0   0   3
