Disk
====

`WMA link <https://reference.wolfram.com/language/ref/Disk.html>`_


:code:`Disk` [{:math:`c_x`, :math:`c_y`}, :math:`r`]
    fills a circle with center (:math:`c_x`, :math:`c_y`) and radius :math:`r`.

:code:`Disk` [{:math:`c_x`, :math:`c_y`}, {:math:`r_x`, :math:`r_y`}]
    fills an ellipse.

:code:`Disk` [{:math:`c_x`, :math:`c_y`}]
    chooses radius 1.

:code:`Disk[]`
    chooses center :math:`(0, 0)`' and radius 1.

:code:`Disk` [{:math:`x`, :math:`y`}, ..., {:math:`t_1`, :math:`t_2`}]
    is a sector from angle :math:`t_1` to :math:`t_2`.





>>> Graphics[{Blue, Disk[{0, 0}, {2, 1}]}]
    =

.. image:: tmp2xdhgpgt.png
    :align: center




The outer border can be drawn using :code:`EdgeForm` :

>>> Graphics[{EdgeForm[Black], Red, Disk[]}]
    =

.. image:: tmpq87oy_so.png
    :align: center




Disk can also draw sectors of circles and ellipses

>>> Graphics[Disk[{0, 0}, 1, {Pi / 3, 2 Pi / 3}]]
    =

.. image:: tmpmzc0rln5.png
    :align: center



>>> Graphics[{Blue, Disk[{0, 0}, {1, 2}, {Pi / 3, 5 Pi / 3}]}]
    =

.. image:: tmpoeowg6rb.png
    :align: center



