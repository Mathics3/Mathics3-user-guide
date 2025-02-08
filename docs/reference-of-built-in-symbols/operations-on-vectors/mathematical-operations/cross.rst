Cross
=====

`Cross product <https://en.wikipedia.org/wiki/Cross_product>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/vector/api/functions.html#sympy.physics.vector.functions.cross>`_, `WMA <https://reference.wolfram.com/language/ref/Cross.html>`_)


:code:`Cross` [:math:`a`, :math:`b`]
    computes the vector cross product of :math:`a` and :math:`b`.





Three-dimensional cross product:

>>> Cross[{x1, y1, z1}, {x2, y2, z2}]
    =

:math:`\left\{\text{y1} \text{z2}-\text{y2} \text{z1},-\text{x1} \text{z2}+\text{x2} \text{z1},\text{x1} \text{y2}-\text{x2} \text{y1}\right\}`



:code:`Cross`  is antisymmetric, so:

>>> Cross[{x, y}]
    =

:math:`\left\{-y,x\right\}`



Graph two-Dimensional cross product:

>>> v1 = {1, Sqrt[3]}; v2 = Cross[v1]
    =

:math:`\left\{-\sqrt{3},1\right\}`



Visualize this:

>>> Graphics[{Arrow[{{0, 0}, v1}], Red, Arrow[{{0, 0}, v2}]}, Axes -> True]
    =

.. image:: tmp8cmv0d4_.png
    :align: center



>>> Clear[v1, v2];
    = `

>>> Cross[{1, 2}, {3, 4, 5}]

    Cross::nonn1 The arguments are expected to be vectors of equal length, and the number of arguments is expected to be 1 less than their length.
    =

:math:`\text{Cross}\left[\left\{1,2\right\},\left\{3,4,5\right\}\right]`


