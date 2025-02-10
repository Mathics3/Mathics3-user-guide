Plot
====

`WMA link <https://reference.wolfram.com/language/ref/Plot.html>`_

:code:`Plot` [:math:`f`, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}]
    plots :math:`f` with :math:`x` ranging from :math:`x_{min}` to :math:`x_{max}`.

:code:`Plot` [{:math:`f_1`, :math:`f_2`, ...}, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}]
    plots several functions :math:`f_1`, :math:`f_2`, ...





>>> Plot[{Sin[x], Cos[x], x / 3}, {x, -Pi, Pi}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_q2n19jya.png
    :align: center



>>> Plot[Sin[x], {x, 0, 4 Pi}, PlotRange->{{0, 4 Pi}, {0, 1.5}}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_5ucgffwo.png
    :align: center



>>> Plot[Tan[x], {x, -6, 6}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_03xru2dt.png
    :align: center



>>> Plot[x^2, {x, -1, 1}, MaxRecursion->5, Mesh->All]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_52p5_duh.png
    :align: center



>>> Plot[Log[x], {x, 0, 5}, MaxRecursion->0]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_pbtzdcmu.png
    :align: center



>>> Plot[Tan[x], {x, 0, 6}, Mesh->All, PlotRange->{{-1, 5}, {0, 15}}, MaxRecursion->10]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_5fdcb8se.png
    :align: center




A constant function:

>>> Plot[3, {x, 0, 1}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot_ldftlctc.png
    :align: center



