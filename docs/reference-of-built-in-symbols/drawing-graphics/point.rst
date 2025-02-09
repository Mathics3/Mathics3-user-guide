Point
=====

`WMA link <https://reference.wolfram.com/language/ref/Point.html>`_


:code:`Point` [{:math:`point_1`, :math:`point_2` ...}]
    represents the point primitive.

:code:`Point` [{{:math:`p_11`, :math:`p_12`, ...}, {:math:`p_21`, :math:`p_22`, ...}, ...}]
    represents a number of point primitives.





Points are rendered if possible as circular regions. Their diameters can be specified using :code:`PointSize` .

Points can be specified as {:math:`x`, :math:`y`}:

>>> Graphics[Point[{0, 0}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Point_feykcl0_.png
    :align: center



>>> Graphics[Point[Table[{Sin[t], Cos[t]}, {t, 0, 2. Pi, Pi / 15.}]]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Point_3e1p6dxo.png
    :align: center




or as {:math:`x`, :math:`y`, :math:`z`}:

>>> Graphics3D[{Orange, PointSize[0.05], Point[Table[{Sin[t], Cos[t], 0}, {t, 0, 2 Pi, Pi / 15.}]]}]

