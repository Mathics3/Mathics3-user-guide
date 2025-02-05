Cylinder
========

`Cylinder <https://en.wikipedia.org/wiki/Cylinder>`_ (`WMA <https://reference.wolfram.com/language/ref/Cylinder.html>`_)


:code:`Cylinder` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}}]
    represents a cylinder of radius 1.

:code:`Cylinder` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}}, :math:`r`]
    represents a cylinder of radius :math:`r` starting at (:math:`x_1`, :math:`y_1`, :math:`z_1`) and ending at           (:math:`x_2`, :math:`y_2`, :math:`z_2`).

:code:`Cylinder` [{{:math:`x_1`, :math:`y_1`, :math:`z_1`}, {:math:`x_2`, :math:`y_2`, :math:`z_2`}, ... }, :math:`r`]
    represents is a collection cylinders of radius :math:`r`.





>>> Graphics3D[Cylinder[{{0, 0, 0}, {1, 1, 1}}, 1]]
  = -Graphics3D-
>>> Graphics3D[{Yellow, Cylinder[{{-1, 0, 0}, {1, 0, 0}, {0, 0, Sqrt[3]}, {1, 1, Sqrt[3]}}, 1]}]
  = -Graphics3D-
