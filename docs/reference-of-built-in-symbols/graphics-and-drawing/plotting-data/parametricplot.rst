ParametricPlot
==============

`WMA link <https://reference.wolfram.com/language/ref/ParametricPlot.html>`_

:code:`ParametricPlot` [{:math:`f_x`, :math:`f_y`}, {:math:`u`, :math:`u_{min}`, :math:`u_{max}`}]
    plots a parametric function :math:`f` with the parameter :math:`u` ranging from :math:`u_{min}` to :math:`u_{max}`.

:code:`ParametricPlot` [{{:math:`f_x`, :math:`f_y`}, {:math:`g_x`, :math:`g_y`}, ...}, {:math:`u`, :math:`u_{min}`, :math:`u_{max}`}]
    plots several parametric functions :math:`f`, :math:`g`, ...

:code:`ParametricPlot` [{:math:`f_x`, :math:`f_y`}, {:math:`u`, :math:`u_{min}`, :math:`u_{max}`}, {:math:`v`, :math:`v_{min}`, :math:`v_{max}`}]
    plots a parametric area.

:code:`ParametricPlot` [{{:math:`f_x`, :math:`f_y`}, {:math:`g_x`, :math:`g_y`}, ...}, {:math:`u`, :math:`u_{min}`, :math:`u_{max}`}, {:math:`v`, :math:`v_{min}`, :math:`v_{max}`}]
    plots several parametric areas.





>>> ParametricPlot[{Sin[u], Cos[3 u]}, {u, 0, 2 Pi}]
    =

.. image:: tmpz4ghz8ax.png
    :align: center



>>> ParametricPlot[{Cos[u] / u, Sin[u] / u}, {u, 0, 50}, PlotRange->0.5]
    =

.. image:: tmpq19llax3.png
    :align: center



>>> ParametricPlot[{{Sin[u], Cos[u]},{0.6 Sin[u], 0.6 Cos[u]}, {0.2 Sin[u], 0.2 Cos[u]}}, {u, 0, 2 Pi}, PlotRange->1, AspectRatio->1]
    =

.. image:: tmp2dgki5ib.png
    :align: center



