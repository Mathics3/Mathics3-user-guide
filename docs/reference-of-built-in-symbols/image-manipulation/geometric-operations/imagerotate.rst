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
.. image:: tmpoitr68po.png
    :align: center



>>> ImageRotate[ein, 45 Degree]

    =
.. image:: tmpqoubq7hz.png
    :align: center



>>> ImageRotate[ein, Pi / 4]

    =
.. image:: tmp4wpc38w3.png
    :align: center



