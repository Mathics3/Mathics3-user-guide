Polygon
=======

`WMA link <https://reference.wolfram.com/language/ref/Polygon.html>`_


:code:`Polygon` [{:math:`point_1`, :math:`point_2` ...}]
    represents the filled polygon primitive.

:code:`Polygon` [{{:math:`p_11`, :math:`p_12`, ...}, {:math:`p_21`, :math:`p_22`, ...}, ...}]
    represents a number of filled polygon primitives.





A Right Triangle:

>>> Graphics[Polygon[{{1,0},{0,0},{0,1}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Polygon_o98_xgyd.png
    :align: center




Notice that there is a line connecting from the last point to the first one.

A point is an element of the polygon if a ray from the point in any direction in     the plane crosses the boundary line segments an odd number of times.

>>> Graphics[Polygon[{{150,0},{121,90},{198,35},{102,35},{179,90}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Polygon_iwdg32tl.png
    :align: center



>>> Graphics3D[Polygon[{{0,0,0},{0,1,1},{1,0,0}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Polygon__5brkdj_.png
    :align: center



