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
.. image:: tmpolwapr_v.png
    :align: center



>>> ImageRotate[ein, 45 Degree]

    =
.. image:: tmp7vxzyo23.png
    :align: center



>>> ImageRotate[ein, Pi / 4]

    =
.. image:: tmpqk9leguo.png
    :align: center



