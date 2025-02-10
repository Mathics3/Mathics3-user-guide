BezierCurve
===========

`WMA link <https://reference.wolfram.com/language/ref/BezierCurve.html>`_


:code:`BezierCurve` [{:math:`pt_1`, :math:`pt_2` ...}]
    represents a Bézier curve with control points :math:`p_i`.

    The result is a curve by combining the Bézier curves when points are taken triples at a time.





Option:


- :code:`SplineDegree->:math:`d``  specifies that the underlying polynomial basis should have maximal degree d.





Set up some points to form a simple zig-zag...

>>> pts = {{0, 0}, {1, 1}, {2, -1}, {3, 0}};



=

>>> Graphics[{Line[pts], Red, Point[pts]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_BezierCurve_fikl3b0f.png
    :align: center




A composite Bézier curve, shown in blue, smooths the zig zag. Control points are shown in red:

>>> Graphics[{BezierCurve[pts], Blue, Line[pts], Red, Point[pts]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_BezierCurve_te42zswo.png
    :align: center




Extend points...

>>> pts = {{0, 0}, {1, 1}, {2, -1}, {3, 0}, {5, 2}, {6, -1}, {7, 3}};



=

A longer composite Bézier curve and its control points:

>>> Graphics[{BezierCurve[pts], Blue, Line[pts], Red, Point[pts]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_BezierCurve_os9f0bu0.png
    :align: center




Notice how the curve from the first to third point is not changed by any points outside the interval. The same is true for points three to five, and so on.

>>> Clear[pts];
    = `

