ListStepPlot
============

`WMA link <https://reference.wolfram.com/language/ref/ListStepPlot.html>`_

:code:`ListStepPlot` [{:math:`y_1`, :math:`y_2`, ...}]
    plots a line through a list of :math:`y`-values, assuming integer :math:`x`-values 1, 2, 3, ...

:code:`ListStepPlot` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    plots a line through a list of :math:`x`, :math:`y` pairs.

:code:`ListStepPlot` [{:math:`list_1`, :math:`list_2`, ...}]
    plots several lines.





>>> ListStepPlot[{1, 1, 2, 3, 5, 8, 13, 21}]

    =
.. image:: tmprniqmk8_.png
    :align: center




:code:`ListStepPlot`  accepts a superset of the Graphics options.     By default, :code:`ListStepPlot` s are joined, but that can be disabled.

>>> ListStepPlot[{1, 1, 2, 3, 5, 8, 13, 21}, Joined->False]

    =
.. image:: tmpog7y2qnw.png
    :align: center




The same as the first example but using a list of point as data,     and filling the plot to the x axis.

>>> ListStepPlot[{{1, 1}, {3, 2}, {4, 5}, {5, 8}, {6, 13}, {7, 21}}, Filling->Axis]

    =
.. image:: tmpjiy0rwm_.png
    :align: center



