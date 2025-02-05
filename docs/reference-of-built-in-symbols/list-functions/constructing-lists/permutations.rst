Permutations
============

`WMA link <https://reference.wolfram.com/language/ref/Permutations.html>`_


:code:`Permutations` [:math:`list`]
    gives all possible orderings of the items in :math:`list`.

:code:`Permutations` [:math:`list`, :math:`n`]
    gives permutations up to length :math:`n`.

:code:`Permutations` [:math:`list`, {:math:`n`}]
    gives permutations of length :math:`n`.





>>> Permutations[{y, 1, x}]
  = {{y, 1, x}, {y, x, 1}, {1, y, x}, {1, x, y}, {x, y, 1}, {x, 1, y}}

Elements are differentiated by their position in :math:`list`, not their value.

>>> Permutations[{a, b, b}]
  = {{a, b, b}, {a, b, b}, {b, a, b}, {b, b, a}, {b, a, b}, {b, b, a}}
>>> Permutations[{1, 2, 3}, 2]
  = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 1}, {2, 3}, {3, 1}, {3, 2}}
>>> Permutations[{1, 2, 3}, {2}]
  = {{1, 2}, {1, 3}, {2, 1}, {2, 3}, {3, 1}, {3, 2}}
