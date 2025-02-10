Darker
======

`WMA link <https://reference.wolfram.com/language/ref/Darker.html>`_


:code:`Darker` [:math:`c`, :math:`f`]
    is equivalent to :code:`Blend` [{:math:`c`, :code:`Black` }, :math:`f`].

:code:`Darker` [:math:`c`]
    is equivalent to :code:`Darker` [:math:`c`, :code:`1/3` ].





>>> Graphics[{Darker[Red], Disk[]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Darker_rzsarogy.png
    :align: center



>>> Graphics3D[{Darker[Green], Sphere[]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Darker_ha597mzq.png
    :align: center



>>> Graphics[Table[{Darker[Yellow, x], Disk[{12x, 0}]}, {x, 0, 1, 1/6}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Darker_xwnd4w3r.png
    :align: center



