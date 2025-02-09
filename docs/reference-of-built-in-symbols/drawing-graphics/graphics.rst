Graphics
========

`WMA link <https://reference.wolfram.com/language/ref/Graphics.html>`_


:code:`Graphics` [:math:`primitives`, :math:`options`]
    represents a graphic.





Options include:



- Axes

- TicksStyle

- AxesStyle

- LabelStyle

- AspectRatio

- PlotRange

- PlotRangePadding

- ImageSize

- Background




>>> Graphics[{Blue, Line[{{0,0}, {1,1}}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Graphics_d1ujnbvs.png
    :align: center




:code:`Graphics`  supports :code:`PlotRange` :

>>> Graphics[{Rectangle[{1, 1}]}, Axes -> True, PlotRange -> {{-2, 1.5}, {-1, 1.5}}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Graphics_9qjmjzc4.png
    :align: center



>>> Graphics[{Rectangle[],Red,Disk[{1,0}]},PlotRange->{{0,1},{0,1}}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Graphics_epl74cx8.png
    :align: center




:code:`Graphics`  produces :code:`GraphicsBox`  boxes:

>>> Graphics[Rectangle[]] // ToBoxes // Head

    =
:math:`\text{GraphicsBox}`



The :code:`Background`  option allows to set the color of the background:

>>> Graphics[{Green, Disk[]}, Background->RGBColor[.6, .7, 1.]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Graphics_7hbi5ysz.png
    :align: center




In :code:`TeXForm` , :code:`Graphics`  produces Asymptote figures:

>>> Graphics[Circle[]] // TeXForm

    =

.. math::
    \text{\newline
    $\backslash$begin\{asy\}\newline
    usepackage("amsmath");\newline
    size(5.869cm, 5.8333cm);\newline
    draw(ellipse((175,175),175,175), rgb(0, 0, 0)+linewidth(1.0667));\newline
    clip(box((-0.53333,0.53333), (350.53,349.47)));\newline
    $\backslash$end\{asy\}\newline
    }



