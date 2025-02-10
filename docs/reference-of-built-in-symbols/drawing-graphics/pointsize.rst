PointSize
=========

`WMA link <https://reference.wolfram.com/language/ref/PointSize.html>`_


:code:`PointSize` [:math:`t`]
    sets the diameter of points to :math:`t`, which is relative to the overall width.





:code:`PointSize`  can be used for both two- and three-dimensional graphics.     The initial default pointsize is 0.008 for two-dimensional graphics and 0.01 for three-dimensional graphics.

>>> Table[Graphics[{PointSize[r], Point[{0, 0}]}], {r, {0.02, 0.05, 0.1, 0.3}}]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Drawing_Graphics_PointSize__7th9v4m.png
    :align: center



>>> Table[Graphics3D[{PointSize[r], Point[{0, 0, 0}]}], {r, {0.05, 0.1, 0.8}}]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Drawing_Graphics_PointSize_02q8gjjp.png
    :align: center



