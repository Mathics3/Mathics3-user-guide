Graphics Introduction Examples
==============================

Two-dimensional graphics can be created using the function :code:`Graphics`  and a list of graphics primitives. For three-dimensional graphics see the following section. The following primitives are available:

:code:`Circle` [{:math:`x`, :math:`y`}, :math:`r`]
    draws a circle.

:code:`Disk` [{:math:`x`, :math:`y`}, :math:`r`]
    draws a filled disk.

:code:`Rectangle` [{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}]
    draws a filled rectangle.

:code:`Polygon` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    draws a filled polygon.

:code:`Line` [{{:math:`x_1`, :math:`y_1`}, {:math:`x_2`, :math:`y_2`}, ...}]
    draws a line.

:code:`Text` [:math:`text`, {:math:`x`, :math:`y`}]
    draws text in a graphics.





>>> Graphics[{Circle[{0, 0}, 1]}]
  = -Graphics-
>>> Graphics[{Line[{{0, 0}, {0, 1}, {1, 1}, {1, -1}}], Rectangle[{0, 0}, {-1, -1}]}]
  = -Graphics-

Colors can be added in the list of graphics primitives to change the drawing color. The following ways to specify colors are supported:

:code:`RGBColor` [:math:`r`, :math:`g`, :math:`b`]
    specifies a color using red, green, and blue.

:code:`CMYKColor` [:math:`c`, :math:`m`, :math:`y`, :math:`k`]
    specifies a color using cyan, magenta, yellow, and black.

:code:`Hue` [:math:`h`, :math:`s`, :math:`b`]
    specifies a color using hue, saturation, and brightness.

:code:`GrayLevel` [:math:`l`]
    specifies a color using a gray level.





All components range from 0 to 1. Each color function can be supplied with an additional argument specifying the desired opacity ("alpha") of the color. There are many predefined colors, such as :code:`Black` , :code:`White` , :code:`Red` , :code:`Green` , :code:`Blue` , etc.

>>> Graphics[{Red, Disk[]}]
  = -Graphics-

Table of hues:

>>> Graphics[Table[{Hue[h, s], Disk[{12h, 8s}]}, {h, 0, 1, 1/6}, {s, 0, 1, 1/4}]]
  = -Graphics-

Colors can be mixed and altered using the following functions:

:code:`Blend` [{:math:`color1`, :math:`color2`}, :math:`ratio`]
    mixes :math:`color1` and :math:`color2` with :math:`ratio`, where a ratio of 0 returns :math:`color1` and a ratio of 1 returns :math:`color2`.

:code:`Lighter` [:math:`color`]
    makes :math:`color` lighter (mixes it with :code:`White` ).

:code:`Darker` [:math:`color`]
    makes :math:`color` darker (mixes it with :code:`Black` ).





>>> Graphics[{Lighter[Red], Disk[]}]
  = -Graphics-

:code:`Graphics`  produces a :code:`GraphicsBox` :

>>> Head[ToBoxes[Graphics[{Circle[]}]]]
  = GraphicsBox
