ImageColorSpace
===============

`WMA link <https://reference.wolfram.com/language/ref/ImageColorSpace.html>`_


:code:`ImageColorSpace` [:math:`image`]
    gives :math:`image`'s color space, e.g. "RGB" or "CMYK".





>>> img = Import["ExampleData/MadTeaParty.gif"];


>>> ImageColorSpace[img]

    =
:math:`\text{Grayscale}`


>>> img = Import["ExampleData/sunflowers.jpg"];


>>> ImageColorSpace[img]

    =
:math:`\text{RGB}`


