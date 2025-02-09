Cuboid
======

`Cuboid <https://en.wikipedia.org/wiki/Cuboid>`_ (`WMA <https://reference.wolfram.com/language/ref/Cuboid.html>`_)

Cuboid also known as interval, rectangle, square, cube, rectangular parallelepiped,     tesseract, orthotope, and box.

:code:`Cuboid` [:math:`p_{min}`]
    is a unit cube/square with its lower corner at point :math:`p_{min}`.

:code:`Cuboid` [:math:`p_{min}`, :math:`p_{max}`]
    is a 2d square with with lower corner :math:`p_{min}` and upper corner :math:`p_{max}`.

:code:`Cuboid` [{:math:`p_{min}`, :math:`p_{max}`}]
    is a cuboid with lower corner :math:`p_{min}` and upper corner :math:`p_{max}`.

:code:`Cuboid` [{:math:`p1_{min}`, :math:`p1_{max}`, ...}]
    is a collection of cuboids.

:code:`Cuboid[]`  is equivalent to :code:`Cuboid` [{0,0,0}].




>>> Graphics3D[Cuboid[{0, 0, 1}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cuboid_u4bmfvjl.png
    :align: center



>>> Graphics3D[{Red, Cuboid[{{0, 0, 0}, {1, 1, 0.5}}], Blue, Cuboid[{{0.25, 0.25, 0.5}, {0.75, 0.75, 1}}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cuboid_e97nkcvh.png
    :align: center



>>> Graphics[Cuboid[{0, 0}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Cuboid_998pgx_y.png
    :align: center



