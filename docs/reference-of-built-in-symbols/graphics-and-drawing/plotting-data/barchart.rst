BarChart
========

`WMA link <https://reference.wolfram.com/language/ref/BarChart.html>`_

:code:`BarChart` [{:math:`b_1`, :math:`b_2` ...}]
    makes a bar chart with lengths :math:`b_1`, :math:`b_2`, ....





Drawing options include -
Charting:


- Mesh

- PlotRange

- ChartLabels

- ChartLegends

- ChartStyle




BarChart specific:


- Axes  (default {False, True})

- AspectRatio: (default 1 / GoldenRatio)




A bar chart of a list of heights:

>>> BarChart[{1, 4, 2}]
    =

.. image:: tmpjr3azakc.png
    :align: center



>>> BarChart[{1, 4, 2}, ChartStyle -> {Red, Green, Blue}]
    =

.. image:: tmps8iejeh2.png
    :align: center



>>> BarChart[{{1, 2, 3}, {2, 3, 4}}]
    =

.. image:: tmpa7m0s_dn.png
    :align: center




Chart several datasets with categorical labels:

>>> BarChart[{{1, 2, 3}, {2, 3, 4}}, ChartLabels -> {"a", "b", "c"}]
    =

.. image:: tmpugh6cgpy.png
    :align: center



>>> BarChart[{{1, 5}, {3, 4}}, ChartStyle -> {{EdgeForm[Thin], White}, {EdgeForm[Thick], White}}]
    =

.. image:: tmpam2gvyz7.png
    :align: center



