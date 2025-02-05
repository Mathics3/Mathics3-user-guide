PieChart
========

`Pie Chart <https://en.wikipedia.org/wiki/Pie_chart>`_     (`WMA link <https://reference.wolfram.com/language/ref/PieChart.html>`_)

:code:`PieChart` [{:math:`a_1`, :math:`a_2` ...}]
    draws a pie chart with sector angles proportional to :math:`a_1`, :math:`a_2`, ....





Drawing options include -
Charting:


- Mesh

- PlotRange

- ChartLabels

- ChartLegends

- ChartStyle




PieChart specific:


- Axes (default: False, False)

- AspectRatio (default 1)

- SectorOrigin: (default {Automatic, 0})

- SectorSpacing" (default Automatic)




A hypothetical comparison between types of pets owned:

>>> PieChart[{30, 20, 10}, ChartLabels -> {Dogs, Cats, Fish}]
  = -Graphics-

A doughnut chart for a list of values:

>>> PieChart[{8, 16, 2}, SectorOrigin -> {Automatic, 1.5}]
  = -Graphics-

A Pie chart with multiple datasets:

>>> PieChart[{{10, 20, 30}, {15, 22, 30}}]
  = -Graphics-

Same as the above, but without gaps between the groups of data:

>>> PieChart[{{10, 20, 30}, {15, 22, 30}}, SectorSpacing -> None]
  = -Graphics-

The doughnut chart above with labels on each of the 3 pieces:

>>> PieChart[{{10, 20, 30}, {15, 22, 30}}, ChartLabels -> {A, B, C}]
  = -Graphics-

Negative values are removed, the data below is the same as {1, 3}:

>>> PieChart[{1, -1, 3}]
  = -Graphics-
