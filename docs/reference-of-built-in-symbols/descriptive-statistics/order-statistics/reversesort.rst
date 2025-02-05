ReverseSort
===========

`WMA link <https://reference.wolfram.com/language/ref/ReverseSort.html>`_


:code:`ReverseSort` [:math:`list`]
    sorts :math:`list` (or the elements of any other expression) according           to reverse canonical ordering.

:code:`ReverseSort` [:math:`list`, :math:`p`]
    sorts using :math:`p` to determine the order of two elements.





>>> ReverseSort[{c, b, d, a}]
  = {d, c, b, a}

You can specify a binary comparison function:

>>> ReverseSort[{1, 2, 0, 3}, Less]
  = {3, 2, 1, 0}

Using :code:`Greater`  for the above, reverses the reverse sort:

>>> ReverseSort[{1, 2, 0, 3}, Greater]
  = {0, 1, 2, 3}

See also `Sort </doc/reference-of-built-in-symbols/descriptive-statistics/order-statistics/sort/>`_.