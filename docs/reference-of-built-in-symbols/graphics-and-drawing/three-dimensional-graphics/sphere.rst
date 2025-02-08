Sphere
======

`WMA link <https://reference.wolfram.com/language/ref/Sphere.html>`_


:code:`Sphere` [{:math:`x`, :math:`y`, :math:`z`}]
    is a sphere of radius 1 centered at the point {:math:`x`, :math:`y`, :math:`z`}.

:code:`Sphere` [{:math:`x`, :math:`y`, :math:`z`}, :math:`r`]
    is a sphere of radius :math:`r` centered at the point {:math:`x`, :math:`y`, :math:`z`}.

:code:`Sphere` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}, ... }, :math:`r`]
    is a collection spheres of radius :math:`r` centered at the points             {:math:`x_1`, :math:`y_2`, :math:`z_2`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}, ...





>>> Graphics3D[Sphere[{0, 0, 0}, 1]]
    =

.. image:: tmpdsnstykp.png
    :align: center



>>> Graphics3D[{Yellow, Sphere[{{-1, 0, 0}, {1, 0, 0}, {0, 0, Sqrt[3.]}}, 1]}]
    =

.. image:: tmpn4lllxka.png
    :align: center



