Plotting Introduction Examples
==============================

\Mathics can plot functions:

>>> Plot[Sin[x], {x, 0, 2 Pi}]

    =
.. image:: asy_Manual_Language_Tutorial_Plotting_Introduction_Examples_a3b7of6v.png
    :align: center




You can also plot multiple functions at once:

>>> Plot[{Sin[x], Cos[x], x ^ 2}, {x, -1, 1}]

    =
.. image:: asy_Manual_Language_Tutorial_Plotting_Introduction_Examples_hh0ab9z2.png
    :align: center




Two-dimensional functions can be plotted using :code:`DensityPlot` :

>>> DensityPlot[x ^ 2 + 1 / y, {x, -1, 1}, {y, 1, 4}]

    =
.. image:: asy_Manual_Language_Tutorial_Plotting_Introduction_Examples_wk7lhasu.png
    :align: center




You can use a custom coloring function:

>>> DensityPlot[x ^ 2 + 1 / y, {x, -1, 1}, {y, 1, 4}, ColorFunction -> (Blend[{Red, Green, Blue}, #]&)]

    =
.. image:: asy_Manual_Language_Tutorial_Plotting_Introduction_Examples_wb_49pu0.png
    :align: center




One problem with :code:`DensityPlot`  is that it's still very slow, basically due to function evaluation being pretty slow in general---and :code:`DensityPlot`  has to evaluate a lot of functions.

Three-dimensional plots are supported as well:

>>> Plot3D[Exp[x] Cos[y], {x, -2, 1}, {y, -Pi, 2 Pi}]

    =
.. image:: asy_Manual_Language_Tutorial_Plotting_Introduction_Examples_ywn64sh3.png
    :align: center



