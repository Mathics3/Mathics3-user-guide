RGBColor
========

`RGB color model <https://en.wikipedia.org/wiki/RGB_color_model>`_ (`WMA link <https://reference.wolfram.com/language/ref/RGBColor.html>`_)


:code:`RGBColor` [:math:`r`, :math:`g`, :math:`b`]
    represents a color with the specified red, green and blue         components. These values should be a number between 0 and 1.         Unless specified using the form below or using `Opacity </doc/reference-of-built-in-symbols/colors/color-directives/opacity>`_,        default opacity is 1, a solid opaque color.

:code:`RGBColor` [:math:`r`, :math:`g`, :math:`b`, :math:`a`]
    Same as above but an opacity value is specified. :math:`a` must have           value between 0 and 1.           :code:`RGBColor[:math:`r`,:math:`g`,:math:`b`,:math:`a`]`  is equivalent to :code:`{RGBColor[:math:`r`,:math:`g`,:math:`b`],Opacity[:math:`a`]}.`






A swatch of color green:

>>> RGBColor[0, 1, 0]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_RGBColor_vcevk79s.png
    :align: center




Let's show what goes on in the process of boxing the above to make this display:

>>> RGBColor[0, 1, 0] // ToBoxes

    =
:math:`\text{StyleBox}\left[\text{GraphicsBox}\left[\left\{\text{EdgeForm}\left[\text{RGBColor}\left[0,0,0\right]\right],\text{RGBColor}\left[0,1,0\right],\text{RectangleBox}\left[\left\{0,0\right\}\right]\right\},\text{AspectRatio}->\text{Automatic},\text{Axes}->\text{False},\text{AxesStyle}->\left\{\right\},\text{Background}->\text{Automatic},\text{ImageSize}->16,\text{LabelStyle}->\left\{\right\},\text{PlotRange}->\text{Automatic},\text{PlotRangePadding}->\text{Automatic},\text{TicksStyle}->\left\{\right\}\right],\text{ImageSizeMultipliers}->\left\{1,1\right\},\text{ShowStringCharacters}->\text{True}\right]`



A swatch of color green which is 1/8 opaque:

>>> RGBColor[0, 1, 0, 0.125]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_RGBColor__2kiwo8m.png
    :align: center




A series of small disks of the primary colors:

>>> Graphics[MapIndexed[{RGBColor @@ #1, Disk[2*#2 ~Join~ {0}]} &, IdentityMatrix[3]], ImageSize->Small]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_RGBColor_7lo0atj9.png
    :align: center



