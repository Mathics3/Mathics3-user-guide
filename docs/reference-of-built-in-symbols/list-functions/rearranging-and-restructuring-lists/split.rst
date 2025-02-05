Split
=====

`WMA link <https://reference.wolfram.com/language/ref/Split.html>`_


:code:`Split` [:math:`list`]
    splits :math:`list` into collections of consecutive identical elements.

:code:`Split` [:math:`list`, :math:`test`]
    splits :math:`list` based on whether the function :math:`test` yields
    :code:`True`  on consecutive elements.





>>> Split[{x, x, x, y, x, y, y, z}]
  = {{x, x, x}, {y}, {x}, {y, y}, {z}}

Split into increasing or decreasing runs of elements

>>> Split[{1, 5, 6, 3, 6, 1, 6, 3, 4, 5, 4}, Less]
  = {{1, 5, 6}, {3, 6}, {1, 6}, {3, 4, 5}, {4}}
>>> Split[{1, 5, 6, 3, 6, 1, 6, 3, 4, 5, 4}, Greater]
  = {{1}, {5}, {6, 3}, {6, 1}, {6, 3}, {4}, {5, 4}}

Split based on first element

>>> Split[{x -> a, x -> y, 2 -> a, z -> c, z -> a}, First[#1] === First[#2] &]
  = {{x -> a, x -> y}, {2 -> a}, {z -> c, z -> a}}
