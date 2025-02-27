Grid
====

`WMA link <https://reference.wolfram.com/language/ref/Grid.html>`_


:code:`Grid` [{{:math:`a_1`, :math:`a_2`, ...}, {:math:`b_1`, :math:`b_2`, ...}, ...}]
    formats several expressions inside a :code:`GridBox` .





>>> Grid[{{a, b}, {c, d}}]

    =
:math:`\begin{array}{cc} a & b\\ c & d\end{array}`



For shallow lists, elements are shown as a column:

>>> Grid[{a, b, c}]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Layout_Grid_jy392g5s.png
    :align: center




If the sublists have different sizes, the grid has the number of columns of the     largest one. Incomplete rows are completed with empty strings:

>>> Grid[{{"first", "second", "third"},{a},{1, 2, 3}}]

    =
:math:`\begin{array}{ccc} \text{first} & \text{second} & \text{third}\\ a &  & \\ 1 & 2 & 3\end{array}`



If the list is a mixture of lists and other expressions, the non-list expressions are
shown as rows:

>>> Grid[{"This is a long title", {"first", "second", "third"},{a},{1, 2, 3}}]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Layout_Grid_6x8m7uri.png
    :align: center



