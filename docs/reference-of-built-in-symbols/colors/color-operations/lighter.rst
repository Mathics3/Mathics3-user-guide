Lighter
=======

`WMA link <https://reference.wolfram.com/language/ref/Lighter.html>`_


:code:`Lighter` [:math:`c`, :math:`f`]
    is equivalent to :code:`Blend` [{:math:`c`, :code:`White` }, :math:`f`].

:code:`Lighter` [:math:`c`]
    is equivalent to :code:`Lighter` [:math:`c`, :code:`1/3` ].





>>> Lighter[Orange, 1/4]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Lighter_e95_94li.png
    :align: center



>>> Graphics[{Lighter[Orange, 1/4], Disk[]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Lighter_6a5bd0nn.png
    :align: center



>>> Graphics[Table[{Lighter[Orange, x], Disk[{12x, 0}]}, {x, 0, 1, 1/6}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Lighter_0j7bp8t_.png
    :align: center



