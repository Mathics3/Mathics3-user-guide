DensityPlot
===========

`WMA link <https://reference.wolfram.com/language/ref/DensityPlot.html>`_

:code:`DensityPlot` [:math:`f`, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}, {:math:`y`, :math:`y_{min}`, :math:`y_{max}`}]
    plots a density plot of :math:`f` with :math:`x` ranging from :math:`x_{min}` to :math:`x_{max}` and :math:`y` ranging from :math:`y_{min}` to :math:`y_{max}`.





>>> DensityPlot[x ^ 2 + 1 / y, {x, -1, 1}, {y, 1, 4}]
  = -Graphics-
>>> DensityPlot[1 / x, {x, 0, 1}, {y, 0, 1}]
  = -Graphics-
>>> DensityPlot[Sqrt[x * y], {x, -1, 1}, {y, -1, 1}]
  = -Graphics-
>>> DensityPlot[1/(x^2 + y^2 + 1), {x, -1, 1}, {y, -2,2}, Mesh->Full]
  = -Graphics-
>>> DensityPlot[x^2 y, {x, -1, 1}, {y, -1, 1}, Mesh->All]
  = -Graphics-
