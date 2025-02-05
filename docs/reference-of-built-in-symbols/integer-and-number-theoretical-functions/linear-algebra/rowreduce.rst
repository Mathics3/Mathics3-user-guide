RowReduce
=========

`WMA link <https://reference.wolfram.com/language/ref/RowReduce.html>`_


:code:`RowReduce` [:math:`matrix`]
    returns the reduced row-echelon form of :math:`matrix`.





>>> RowReduce[{{1, 0, a}, {1, 1, b}}]
  = {{1, 0, a}, {0, 1, -a + b}}
>>> RowReduce[{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}] // MatrixForm
  = 1   0   -1
    
    0   1   2
    
    0   0   0
