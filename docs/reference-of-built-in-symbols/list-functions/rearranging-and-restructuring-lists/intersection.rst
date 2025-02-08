Intersection
============

`WMA link <https://reference.wolfram.com/language/ref/Intersection.html>`_


:code:`Intersection` [:math:`a`, :math:`b`, ...]
    gives the intersection of the sets. The resulting list       will be sorted and each element will only occur once.





>>> Intersection[{1000, 100, 10, 1}, {1, 5, 10, 15}]
    =

:math:`\left\{1,10\right\}`


>>> Intersection[{{a, b}, {x, y}}, {{x, x}, {x, y}, {x, z}}]
    =

:math:`\left\{\left\{x,y\right\}\right\}`


>>> Intersection[{c, b, a}]
    =

:math:`\left\{a,b,c\right\}`


>>> Intersection[{1, 2, 3}, {2, 3, 4}, SameTest->Less]
    =

:math:`\left\{3\right\}`


