BezierFunction
==============

`WMA link <https://reference.wolfram.com/language/ref/BezierFunction.html>`_

:code:`BezierFunction` [{:math:`pt_1`, :math:`pt_2`, ...}]
    returns a Bézier function for the curve defined by points :math:`pt_i`.
    The embedding dimension for the curve represented by :code:`BezierFunction[{:math:`pt_1`,:math:`pt_2`,...}]`  is given by the length of the lists :math:`pt_i`.





>>> f = BezierFunction[{{0, 0}, {1, 1}, {2, 0}, {3, 2}}];



=

>>> f[.5]

    =
:math:`\left\{1.5,0.625\right\}`


>>> Clear[f];
    = `


=


Plotting the Bézier Function accoss a Bézier curve:

>>> Module[{p={{0, 0},{1, 1},{2, -1},{4, 0}}}, Graphics[{BezierCurve[p], Red, Point[Table[BezierFunction[p][x], {x, 0, 1, 0.1}]]}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_BezierFunction_s21o8qn4.png
    :align: center



