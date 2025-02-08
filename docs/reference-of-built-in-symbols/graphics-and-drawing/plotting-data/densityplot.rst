DensityPlot
===========

`WMA link <https://reference.wolfram.com/language/ref/DensityPlot.html>`_

:code:`DensityPlot` [:math:`f`, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}, {:math:`y`, :math:`y_{min}`, :math:`y_{max}`}]
    plots a density plot of :math:`f` with :math:`x` ranging from :math:`x_{min}` to :math:`x_{max}` and :math:`y` ranging from :math:`y_{min}` to :math:`y_{max}`.





>>> DensityPlot[x ^ 2 + 1 / y, {x, -1, 1}, {y, 1, 4}]
    =

.. image:: tmpth_sel9c.png
    :align: center



>>> DensityPlot[1 / x, {x, 0, 1}, {y, 0, 1}]
    =

.. image:: tmp3ftosxye.png
    :align: center



>>> DensityPlot[Sqrt[x * y], {x, -1, 1}, {y, -1, 1}]
    =

.. image:: tmphenc77cf.png
    :align: center



>>> DensityPlot[1/(x^2 + y^2 + 1), {x, -1, 1}, {y, -2,2}, Mesh->Full]
    =

.. image:: tmp_bm10okp.png
    :align: center



>>> DensityPlot[x^2 y, {x, -1, 1}, {y, -1, 1}, Mesh->All]
    =

.. image:: tmp_e8ela3c.png
    :align: center



