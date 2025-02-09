Circle
======

`WMA link <https://reference.wolfram.com/language/ref/Circle.html>`_


:code:`Circle` [{:math:`c_x`, :math:`c_y`}, :math:`r`]
    draws a circle with center :code:`(:math:`c_x`, :math:`c_y`)`  and radius :math:`r`.

:code:`Circle` [{:math:`c_x`, :math:`c_y`}, {:math:`r_x`, :math:`r_y`}]
    draws an ellipse.

:code:`Circle` [{:math:`c_x`, :math:`c_y`}]
    chooses radius 1.

:code:`Circle[]`
    chooses center :code:`(0, 0)`  and radius 1.





>>> Graphics[{Red, Circle[{0, 0}, {2, 1}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Circle_38qcx98i.png
    :align: center



>>> Graphics[{Circle[], Disk[{0, 0}, {1, 1}, {0, 2.1}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Circle_k52caeel.png
    :align: center




Target practice:

>>> Graphics[Circle[], Axes-> True]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Circle_3b3097jy.png
    :align: center



