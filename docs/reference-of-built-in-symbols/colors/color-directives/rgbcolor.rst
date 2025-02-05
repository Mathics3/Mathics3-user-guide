RGBColor
========

`RGB color model <https://en.wikipedia.org/wiki/RGB_color_model>`_ (`WMA link <https://reference.wolfram.com/language/ref/RGBColor.html>`_)


:code:`RGBColor` [:math:`r`, :math:`g`, :math:`b`]
    represents a color with the specified red, green and blue         components. These values should be a number between 0 and 1.         Unless specified using the form below or using `Opacity </doc/reference-of-built-in-symbols/colors/color-directives/opacity>`_,        default opacity is 1, a solid opaque color.

:code:`RGBColor` [:math:`r`, :math:`g`, :math:`b`, :math:`a`]
    Same as above but an opacity value is specified. :math:`a` must have           value between 0 and 1.           :code:`RGBColor[:math:`r`,:math:`g`,:math:`b`,:math:`a`]`  is equivalent to :code:`{RGBColor[:math:`r`,:math:`g`,:math:`b`],Opacity[:math:`a`]}.`






A swatch of color green:

>>> RGBColor[0, 1, 0]
  = RGBColor[0, 1, 0]

Let's show what goes on in the process of boxing the above to make this display:

>>> RGBColor[0, 1, 0] // ToBoxes
  = StyleBox[GraphicsBox[...], ...]

A swatch of color green which is 1/8 opaque:

>>> RGBColor[0, 1, 0, 0.125]
  = RGBColor[0, 1, 0, 0.125]

A series of small disks of the primary colors:

>>> Graphics[MapIndexed[{RGBColor @@ #1, Disk[2*#2 ~Join~ {0}]} &, IdentityMatrix[3]], ImageSize->Small]
  = -Graphics-
