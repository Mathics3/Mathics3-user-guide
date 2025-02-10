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
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Disk_ack9wfq7.png
    :align: center




The outer border can be drawn using :code:`EdgeForm` :

>>> Graphics[{EdgeForm[Black], Red, Disk[]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Disk_9bp1vb_c.png
    :align: center




Disk can also draw sectors of circles and ellipses

>>> Graphics[Disk[{0, 0}, 1, {Pi / 3, 2 Pi / 3}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Disk_4yi_p3a_.png
    :align: center



>>> Graphics[{Blue, Disk[{0, 0}, {1, 2}, {Pi / 3, 5 Pi / 3}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Disk_f8w2ra3r.png
    :align: center



