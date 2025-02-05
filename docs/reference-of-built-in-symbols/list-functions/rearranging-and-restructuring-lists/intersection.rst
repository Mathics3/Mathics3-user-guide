Intersection
============

`WMA link <https://reference.wolfram.com/language/ref/Intersection.html>`_


:code:`Intersection` [:math:`a`, :math:`b`, ...]
    gives the intersection of the sets. The resulting list       will be sorted and each element will only occur once.





>>> Intersection[{1000, 100, 10, 1}, {1, 5, 10, 15}]
  = {1, 10}
>>> Intersection[{{a, b}, {x, y}}, {{x, x}, {x, y}, {x, z}}]
  = {{x, y}}
>>> Intersection[{c, b, a}]
  = {a, b, c}
>>> Intersection[{1, 2, 3}, {2, 3, 4}, SameTest->Less]
  = {3}
