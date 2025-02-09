PlotRange
=========

`WMA link <https://reference.wolfram.com/language/ref/PlotRange.html>`_


:code:`PlotRange`
    is a charting option, such as for :code:`Plot` , :code:`BarChart` , :code:`PieChart` ,           etc. that gives the range of coordinates to include in a plot.







- All all points are included.

- Automatic - outlying points are dropped.

- :math:`max` - explicit limit for each function.

- {:math:`min`, :math:`max`} - explicit limits for :math:`y` (2D), :math:`z` (3D),           or array values.

- {{:math:`x_{min}`, :math:`x_{max}`}, {{:math:`y_{min}`}, {:math:`y_{max}`}} - explicit limits for           :math:`x` and :math:`y`.




>>> Plot[Sin[Cos[x^2]],{x,-4,4}, PlotRange -> All]

    =
.. image:: tmpp03tt15p.png
    :align: center



>>> Graphics[Disk[], PlotRange -> {{-.5, .5}, {0, 1.5}}]

    =
.. image:: tmprtabsdvc.png
    :align: center



