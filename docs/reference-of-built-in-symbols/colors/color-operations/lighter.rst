Lighter
=======

`WMA link <https://reference.wolfram.com/language/ref/Lighter.html>`_


:code:`Lighter` [:math:`c`, :math:`f`]
    is equivalent to :code:`Blend` [{:math:`c`, :code:`White` }, :math:`f`].

:code:`Lighter` [:math:`c`]
    is equivalent to :code:`Lighter` [:math:`c`, :code:`1/3` ].





>>> Lighter[Orange, 1/4]

    =
.. image:: tmphacv2_v8.png
    :align: center



>>> Graphics[{Lighter[Orange, 1/4], Disk[]}]

    =
.. image:: tmpqw3s4iys.png
    :align: center



>>> Graphics[Table[{Lighter[Orange, x], Disk[{12x, 0}]}, {x, 0, 1, 1/6}]]

    =
.. image:: tmp_yrjuyt0.png
    :align: center



