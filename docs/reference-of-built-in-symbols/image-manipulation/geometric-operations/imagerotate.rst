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
.. image:: tmpd20dzmah.png
    :align: center



>>> ImageRotate[ein, 45 Degree]

    =
.. image:: tmphbrh15po.png
    :align: center



>>> ImageRotate[ein, Pi / 4]

    =
.. image:: tmpy5_grm5x.png
    :align: center



