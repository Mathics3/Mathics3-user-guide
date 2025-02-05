SortBy
======

`WMA link <https://reference.wolfram.com/language/ref/SortBy.html>`_


:code:`SortBy` [:math:`list`, :math:`f`]
    sorts :math:`list` (or the elements of any other expression) according to          canonical ordering of the keys that are extracted from the :math:`list`'s          elements using :math:`f`. Chunks of elements that appear the same under :math:`f`          are sorted according to their natural order (without applying :math:`f`).

:code:`SortBy` [:math:`f`]
    creates an operator function that, when applied, sorts by :math:`f`.





>>> SortBy[{{5, 1}, {10, -1}}, Last]
  = {{10, -1}, {5, 1}}
>>> SortBy[Total][{{5, 1}, {10, -9}}]
  = {{10, -9}, {5, 1}}
