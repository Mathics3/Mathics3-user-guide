ImageRotate
===========

`WMA link <https://reference.wolfram.com/language/ref/ImageRotate.html>`_


:code:`ImageRotate` [:math:`image`]
    Rotates :math:`image` 90 degrees counterclockwise.

:code:`ImageRotate` [:math:`image`, :math:`theta`]
    Rotates :math:`image` by a given angle :math:`theta`





>>> ein = Import["ExampleData/Einstein.jpg"];


>>> ImageRotate[ein]

    =
.. image:: tmpxp852mdv.png
    :align: center



>>> ImageRotate[ein, 45 Degree]

    =
.. image:: tmpv5eyfn15.png
    :align: center



>>> ImageRotate[ein, Pi / 4]

    =
.. image:: tmp282ub01i.png
    :align: center



