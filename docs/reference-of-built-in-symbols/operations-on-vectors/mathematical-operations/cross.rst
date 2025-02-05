Cross
=====

`Cross product <https://en.wikipedia.org/wiki/Cross_product>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/vector/api/functions.html#sympy.physics.vector.functions.cross>`_, `WMA <https://reference.wolfram.com/language/ref/Cross.html>`_)


:code:`Cross` [:math:`a`, :math:`b`]
    computes the vector cross product of :math:`a` and :math:`b`.





Three-dimensional cross product:

>>> Cross[{x1, y1, z1}, {x2, y2, z2}]
  = {y1 z2 - y2 z1, -x1 z2 + x2 z1, x1 y2 - x2 y1}

:code:`Cross`  is antisymmetric, so:

>>> Cross[{x, y}]
  = {-y, x}

Graph two-Dimensional cross product:

>>> v1 = {1, Sqrt[3]}; v2 = Cross[v1]
  = {-Sqrt[3], 1}

Visualize this:

>>> Graphics[{Arrow[{{0, 0}, v1}], Red, Arrow[{{0, 0}, v2}]}, Axes -> True]
  = -Graphics-
>>> Clear[v1, v2];

>>> Cross[{1, 2}, {3, 4, 5}]
  = Cross[{1, 2}, {3, 4, 5}]
