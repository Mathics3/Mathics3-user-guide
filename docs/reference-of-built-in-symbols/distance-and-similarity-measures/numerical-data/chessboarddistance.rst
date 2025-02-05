ChessboardDistance
==================

`Chebyshev distance <https://en.wikipedia.org/wiki/Chebyshev_distance>`_     (`WMA <https://reference.wolfram.com/language/ref/ChessboardDistance.html>`_)


:code:`ChessboardDistance` [:math:`u`, :math:`v`]
    returns the chessboard distance (also known as Chebyshev distance) between :math:`u` and :math:`v`, which is the number of moves a king on a chessboard needs to get from square :math:`u` to square :math:`v`.





>>> ChessboardDistance[-7, 5]
  = 12
>>> ChessboardDistance[{-1, -1}, {1, 1}]
  = 2
