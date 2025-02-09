ImageReflect
============

`WMA link <https://reference.wolfram.com/language/ref/ImageReflect.html>`_

:code:`ImageReflect` [:math:`image`]
    Flips :math:`image` top to bottom.

:code:`ImageReflect` [:math:`image`, :math:`side`]
    Flips :math:`image` so that :math:`side` is interchanged with its opposite.

:code:`ImageReflect` [:math:`image`, :math:`side_1` -> :math:`side_2`]
    Flips :math:`image` so that :math:`side_1` is interchanged with :math:`side_2`.





>>> ein = Import["ExampleData/Einstein.jpg"];


>>> ImageReflect[ein]

    =
.. image:: tmp0r6nzboo.png
    :align: center



>>> ImageReflect[ein, Left]

    =
.. image:: tmpx924eoyi.png
    :align: center



>>> ImageReflect[ein, Left -> Top]

    =
.. image:: tmpzz4k8v7c.png
    :align: center



