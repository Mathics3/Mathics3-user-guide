Blend
=====

`WMA link <https://reference.wolfram.com/language/ref/Blend.html>`_


:code:`Blend` [{:math:`c_1`, :math:`c_2`}]
    represents the color between :math:`c_1` and :math:`c_2`.

:code:`Blend` [{:math:`c_1`, :math:`c_2`}, :math:`x`]
    represents the color formed by blending :math:`c_1` and :math:`c_2` with
    factors 1 - :math:`x` and :math:`x` respectively.

:code:`Blend` [{:math:`c_1`, :math:`c_2`, ..., :math:`c_n`}, :math:`x`]
    blends between the colors :math:`c_1` to :math:`c_n` according to the
    factor :math:`x`.





>>> Blend[{Red, Blue}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Blend_bwy24_27.png
    :align: center



>>> Blend[{Red, Blue}, 0.3]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Blend_ad0z_szx.png
    :align: center



>>> Blend[{Red, Blue, Green}, 0.75]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Blend_gbo2qjfj.png
    :align: center



>>> Graphics[Table[{Blend[{Red, Green, Blue}, x], Rectangle[{10 x, 0}]}, {x, 0, 1, 1/10}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Blend_hnwk7y2x.png
    :align: center



>>> Graphics[Table[{Blend[{RGBColor[1, 0.5, 0, 0.5], RGBColor[0, 0, 1, 0.5]}, x], Disk[{5x, 0}]}, {x, 0, 1, 1/10}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Blend_n2rycqy6.png
    :align: center



>>> Blend[{Red, Green, Blue}, {1, 0.5}]
    = Blend[{RGBColor[1, 0, 0], RGBColor[0, 1, 0], RGBColor[0, 0, 1]}, {1, 0.5}]`

