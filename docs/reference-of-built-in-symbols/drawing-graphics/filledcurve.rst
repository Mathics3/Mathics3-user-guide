FilledCurve
===========

`WMA link <https://reference.wolfram.com/language/ref/FilledCurve.html>`_


:code:`FilledCurve` [{:math:`segment_1`, :math:`segment_2` ...}]
    represents a filled curve.





>>> Graphics[FilledCurve[{Line[{{0, 0}, {1, 1}, {2, 0}}]}]]
  = -Graphics-
>>> Graphics[FilledCurve[{BezierCurve[{{0, 0}, {1, 1}, {2, 0}}], Line[{{3, 0}, {0, 2}}]}]]
  = -Graphics-
