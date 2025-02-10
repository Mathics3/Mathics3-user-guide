ListPlot
========

`WMA link <https://reference.wolfram.com/language/ref/ListPlot.html>`_

:code:`ListPlot` [{:math:`y_1`, :math:`y_2`, ...}]
    plots a list of y-values, assuming integer x-values 1, 2, 3, ...

:code:`ListPlot` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    plots a list of :math:`x`, :math:`y` pairs.

:code:`ListPlot` [{:math:`list_1`, :math:`list_2`, ...}]
    plots several lists of points.





The frequency of Primes:

>>> ListPlot[Prime[Range[30]]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListPlot_4lb37xb0.png
    :align: center




seems very roughly to fit a table of quadradic numbers:

>>> ListPlot[Table[n ^ 2 / 8, {n, 30}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListPlot_z_ezvwds.png
    :align: center




ListPlot accepts some Graphics options:

>>> ListPlot[Table[n ^ 2, {n, 30}], Joined->True]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListPlot_w5zmiwxf.png
    :align: center




Compare with `:code:`Plot`  </doc/reference-of-built-in-symbols/graphics-and-drawing/plotting-data/plot/>`_.

>>> ListPlot[Table[n ^ 2, {n, 30}], Filling->Axis]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ListPlot_k41ompfg.png
    :align: center




Compare with `:code:`Plot`  </doc/reference-of-built-in-symbols/graphics-and-drawing/plotting-data/plot>`_.