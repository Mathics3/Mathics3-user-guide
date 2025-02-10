Cone
====

`Cone <https://en.wikipedia.org/wiki/Cone>`_ (`WMA <https://reference.wolfram.com/language/ref/Cone.html>`_)


:code:`Cone` []
    is a cone of radius 1 and height 2 oriented in the upward :math:`z` direction.

:code:`Cone` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}}, :math:`r`]
    is a cone of radius :math:`r` starting at (:math:`x_1`, :math:`y_1`, :math:`z_1`) and ending at           (:math:`x_2`, :math:`y_2`, :math:`z_2`).

:code:`Cone` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}, ... }, :math:`r`]
    is a collection cones of radius :math:`r`.





>>> Graphics3D[Cone[]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cone_r2079637.png
    :align: center



>>> Graphics3D[Cone[{{0, 0, 0}, {1, 1, 1}}, 1]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cone_srs9lzgw.png
    :align: center



>>> Graphics3D[{Yellow, Cone[{{-1, 0, 0}, {1, 0, 0}, {0, 0, Sqrt[3]}, {1, 1, Sqrt[3]}}, 1]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cone_mixaxfof.png
    :align: center



