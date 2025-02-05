PowersRepresentations
=====================

`WMA <https://reference.wolfram.com/language/ref/PowersRepresentations.html>`_

:code:`PowersRepresentations` [:math:`n`, :math:`k`, :math:`p`]
    represent :math:`n` as a sum of :math:`k` non-negative integers raised to the power of :math:`p`.





Get the ways licence plate number 1729 can be represented as the sum of two cubes:

>>> PowersRepresentations[1729, 2, 3]
  = {{1, 12}, {9, 10}}

See `1729 <https://en.wikipedia.org/wiki/1729_(number)>`_ for the full backstory.

Demonstrate the validity of the Pythagorian triple: 3^2 + 4^2 == 5^2

>>> PowersRepresentations[25, 2, 2]
  = {{0, 5}, {3, 4}}

Since 0 is allowed in the sum, :code:`PowersRepresentations[:math:`n`, :math:`k`+1, :math:`p`]`  is includes    :code:`PowersRepresentations[:math:`n`, :math:`k`, :math:`p`]`  with by inserting a zero element at the beginning:

>>> PowersRepresentations[25, 3, 2]
  = {{0, 0, 5}, {0, 3, 4}}
