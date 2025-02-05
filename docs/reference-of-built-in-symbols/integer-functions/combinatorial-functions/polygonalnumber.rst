PolygonalNumber
===============

`Polygonal number <https://en.wikipedia.org/wiki/Polygonal_number>`_ (`WMA <https://reference.wolfram.com/language/ref/PolygonalNumber.html>`_)

:code:`PolygonalNumber` [:math:`n`]
    gives the :math:`n`-th triangular number.

:code:`PolygonalNumber` [:math:`r`, :math:`n`]
    gives the :math:`n`-th :math:`r`-gonal number.





>>> Table[PolygonalNumber[n], {n, 10}]
  = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55}

The sum of two consecutive Polygonal numbers is the square of the larger number:

>>> Table[PolygonalNumber[n-1] + PolygonalNumber[n], {n, 10}]
  = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

:code:`PolygonalNumber` [:math:`r`, :math:`n`] can be interpreted as the number of points arranged in the form of :math:`n`-1 polygons of :math:`r` sides.

List the tenth :math:`r`-gonal number of regular polygons from 3 to 8:

>>> Table[PolygonalNumber[r, 10], {r, 3, 8}]
  = {55, 100, 145, 190, 235, 280}

See also `Binomial </doc/reference-of-built-in-symbols/integer-functions/combinatorial-functions/binomial/>`_, and `RegularPolygon </doc/reference-of-built-in-symbols/drawing-graphics/regularpolygon/>`_.