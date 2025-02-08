ImageType
=========

`WMA link <https://reference.wolfram.com/language/ref/ImageType.html>`_


:code:`ImageType` [:math:`image`]
    gives the interval storage type of :math:`image`, e.g. "Real", "Bit32", or "Bit".





>>> img = Import["ExampleData/hedy.tif"];


>>> ImageType[img]
    =

:math:`\text{Byte}`


>>> ImageType[Image[{{0, 1}, {1, 0}}]]
    =

:math:`\text{Real}`


>>> ImageType[Binarize[img]]
    = Bit`

