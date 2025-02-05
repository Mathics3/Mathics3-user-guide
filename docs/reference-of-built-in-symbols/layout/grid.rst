Grid
====

`WMA link <https://reference.wolfram.com/language/ref/Grid.html>`_


:code:`Grid` [{{:math:`a_1`, :math:`a_2`, ...}, {:math:`b_1`, :math:`b_2`, ...}, ...}]
    formats several expressions inside a :code:`GridBox` .





>>> Grid[{{a, b}, {c, d}}]
  = a   b
    
    c   d

For shallow lists, elements are shown as a column:

>>> Grid[{a, b, c}]
  = a
    
    b
    
    c

If the sublists have different sizes, the grid has the number of columns of the     largest one. Incomplete rows are completed with empty strings:

>>> Grid[{{"first", "second", "third"},{a},{1, 2, 3}}]
  = first   second   third
    
    a
    
    1       2        3

If the list is a mixture of lists and other expressions, the non-list expressions are
shown as rows:

>>> Grid[{"This is a long title", {"first", "second", "third"},{a},{1, 2, 3}}]
  = This is a long title
    
    first   second   third
    
    a
    
    1       2        3
