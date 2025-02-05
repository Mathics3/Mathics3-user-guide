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
  = -Graphics-

:code:`Graphics`  supports :code:`PlotRange` :

>>> Graphics[{Rectangle[{1, 1}]}, Axes -> True, PlotRange -> {{-2, 1.5}, {-1, 1.5}}]
  = -Graphics-
>>> Graphics[{Rectangle[],Red,Disk[{1,0}]},PlotRange->{{0,1},{0,1}}]
  = -Graphics-

:code:`Graphics`  produces :code:`GraphicsBox`  boxes:

>>> Graphics[Rectangle[]] // ToBoxes // Head
  = GraphicsBox

The :code:`Background`  option allows to set the color of the background:

>>> Graphics[{Green, Disk[]}, Background->RGBColor[.6, .7, 1.]]
  = -Graphics-

In :code:`TeXForm` , :code:`Graphics`  produces Asymptote figures:

>>> Graphics[Circle[]] // TeXForm
  = 
    \begin{asy}
    usepackage("amsmath");
    size(5.869cm, 5.8333cm);
    draw(ellipse((175,175),175,175), rgb(0, 0, 0)+linewidth(1.0667));
    clip(box((-0.53333,0.53333), (350.53,349.47)));
    \end{asy}
