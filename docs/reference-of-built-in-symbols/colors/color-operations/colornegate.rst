ColorNegate
===========

Color Inversion (`WMA link <https://reference.wolfram.com/language/ref/ColorNegate.html>`_)


:code:`ColorNegate` [:math:`color`]
    returns the negative of a color, that is, the RGB color           subtracted from white.

:code:`ColorNegate` [:math:`image`]
    returns an image where each pixel has its color negated.





Yellow is :code:`RGBColor[1.0, 1.0, 0.0]`  So when inverted or subtracted     from :code:`White` , we get blue:

>>> ColorNegate[Yellow] == Blue
  = True
>>> ColorNegate[Import["ExampleData/sunflowers.jpg"]]
  = -Image-
