EuclideanDistance
=================

`Euclidean similarity <https://en.wikipedia.org/wiki/Euclidean_distance>`_     (`WMA <https://reference.wolfram.com/language/ref/EuclideanDistance.html>`_)


:code:`EuclideanDistance` [:math:`u`, :math:`v`]
    returns the euclidean distance between :math:`u` and :math:`v`.





>>> EuclideanDistance[-7, 5]
  = 12
>>> EuclideanDistance[{-1, -1}, {1, 1}]
  = 2 Sqrt[2]
>>> EuclideanDistance[{a, b}, {c, d}]
  = Sqrt[Abs[a - c] ^ 2 + Abs[b - d] ^ 2]
