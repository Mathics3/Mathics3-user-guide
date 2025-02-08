ListLogPlot
===========

`WMA link <https://reference.wolfram.com/language/ref/ListLogPlot.html>`_

:code:`ListLogPlot` [{:math:`y_1`, :math:`y_2`, ...}]
    log plots a list of y-values, assuming integer x-values 1, 2, 3, ...

:code:`ListLogPlot` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    log plots a list of :math:`x`, :math:`y` pairs.

:code:`ListLogPlot` [{:math:`list_1`, :math:`list_2`, ...}]
    log plots several lists of points.





Plotting table of Fibonacci numbers:

>>> ListLogPlot[Table[Fibonacci[n], {n, 10}]]
    =

.. image:: tmp0v_82n78.png
    :align: center




we see that Fibonacci numbers grow exponentially. So when     plotted using on a log scale the result fits     points of a sloped line.

>>> ListLogPlot[Table[n!, {n, 10}], Joined -> True]
    =

.. image:: tmpud43eh00.png
    :align: center



