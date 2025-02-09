3D Graphics
===========

Three-dimensional graphics are created using the function :code:`Graphics3D`  and a list of 3D primitives. The following primitives are supported so far:

:code:`Polygon` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_3`}, ...}]
    draws a filled polygon.

:code:`Line` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_3`}, ...}]
    draws a line.

:code:`Point` [{:math:`x_1`, :math:`y_1`, :math:`z_1`}]
    draws a point.





>>> Graphics3D[Polygon[{{0,0,0}, {0,1,1}, {1,0,0}}]]

    =
.. image:: tmpouet69sx.png
    :align: center




Colors can also be added to three-dimensional primitives.

>>> Graphics3D[{Orange, Polygon[{{0,0,0}, {1,1,1}, {1,0,0}}]}, Axes->True]

    =
.. image:: tmppebt78xy.png
    :align: center




:code:`Graphics3D`  produces a :code:`Graphics3DBox` :

>>> Head[ToBoxes[Graphics3D[{Polygon[]}]]]

    =
:math:`\text{Graphics3DBox}`


