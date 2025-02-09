Plot3D
======

`WMA link <https://reference.wolfram.com/language/ref/Plot3D.html>`_

:code:`Plot3D` [:math:`f`, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}, {:math:`y`, :math:`y_{min}`, :math:`y_{max}`}]
    creates a three-dimensional plot of :math:`f` with :math:`x` ranging from :math:`x_{min}` to           :math:`x_{max}` and :math:`y` ranging from :math:`y_{min}` to :math:`y_{max}`.
    
    See `Drawing Option and Option Values </doc/reference-of-built-in-symbols/graphics-and-drawing/drawing-options-and-option-values>`_ for a list of Plot options.





>>> Plot3D[x ^ 2 + 1 / y, {x, -1, 1}, {y, 1, 4}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot3D_ecgyr3jq.png
    :align: center



>>> Plot3D[Sin[y + Sin[3 x]], {x, -2, 2}, {y, -2, 2}, PlotPoints->20]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot3D_30kvn0on.png
    :align: center



>>> Plot3D[x / (x ^ 2 + y ^ 2 + 1), {x, -2, 2}, {y, -2, 2}, Mesh->None]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot3D_048st3rr.png
    :align: center



>>> Plot3D[Sin[x y] /(x y), {x, -3, 3}, {y, -3, 3}, Mesh->All]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot3D_kmx04m82.png
    :align: center



>>> Plot3D[Log[x + y^2], {x, -1, 1}, {y, -1, 1}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Plot3D_8zdq0x0e.png
    :align: center



