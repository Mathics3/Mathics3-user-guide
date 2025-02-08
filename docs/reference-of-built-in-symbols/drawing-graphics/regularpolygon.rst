RegularPolygon
==============

`WMA link <https://reference.wolfram.com/language/ref/RegularPolygon.html>`_


:code:`RegularPolygon` [:math:`n`]
    gives the regular polygon with :math:`n` edges.

:code:`RegularPolygon` [:math:`r`, :math:`n`]
    gives the regular polygon with :math:`n` edges and radius :math:`r`.

:code:`RegularPolygon` [{:math:`r`, :math:`\phi`}, :math:`n`]
    gives the regular polygon with radius :math:`r` with one vertex drawn at angle :math:`\phi`.

:code:`RegularPolygon` [{:math:`x`, :math:`y`}, :math:`r`, :math:`n`]
    gives the regular polygon centered at the position {:math:`x`, :math:`y`}.





>>> Graphics[RegularPolygon[5]]
    =

.. image:: tmp47kui82_.png
    :align: center



>>> Graphics[{Yellow, Rectangle[], Orange, RegularPolygon[{1, 1}, {0.25, 0}, 3]}]
    =

.. image:: tmpv07jtjvo.png
    :align: center



