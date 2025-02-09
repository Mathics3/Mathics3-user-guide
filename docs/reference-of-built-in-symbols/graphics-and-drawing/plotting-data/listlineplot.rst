ListLinePlot
============

`WMA link <https://reference.wolfram.com/language/ref/ListLinePlot.html>`_

:code:`ListLinePlot` [{:math:`y_1`, :math:`y_2`, ...}]
    plots a line through a list of :math:`y`-values, assuming integer :math:`x`-values 1, 2, 3, ...

:code:`ListLinePlot` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    plots a line through a list of :math:`x`, :math:`y` pairs.

:code:`ListLinePlot` [{:math:`list_1`, :math:`list_2`, ...}]
    plots several lines.





>>> ListLinePlot[Table[{n, n ^ 0.5}, {n, 10}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListLinePlot_o99wl0n8.png
    :align: center




ListPlot accepts a superset of the Graphics options.

>>> ListLinePlot[{{-2, -1}, {-1, -1}, {1, 3}}, Filling->Axis]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListLinePlot_mqb40na8.png
    :align: center



