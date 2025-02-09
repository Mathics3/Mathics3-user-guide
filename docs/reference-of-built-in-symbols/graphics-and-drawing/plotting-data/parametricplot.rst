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
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ParametricPlot_skxu8hvb.png
    :align: center



>>> ParametricPlot[{Cos[u] / u, Sin[u] / u}, {u, 0, 50}, PlotRange->0.5]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ParametricPlot_zj3pr4_c.png
    :align: center



>>> ParametricPlot[{{Sin[u], Cos[u]},{0.6 Sin[u], 0.6 Cos[u]}, {0.2 Sin[u], 0.2 Cos[u]}}, {u, 0, 2 Pi}, PlotRange->1, AspectRatio->1]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_ParametricPlot_8i7len82.png
    :align: center



