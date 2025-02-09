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
.. image:: tmpmwxqymy5.png
    :align: center



>>> Graphics[{Circle[], Disk[{0, 0}, {1, 1}, {0, 2.1}]}]

    =
.. image:: tmpgpz884jk.png
    :align: center




Target practice:

>>> Graphics[Circle[], Axes-> True]

    =
.. image:: tmp80etc2yp.png
    :align: center



