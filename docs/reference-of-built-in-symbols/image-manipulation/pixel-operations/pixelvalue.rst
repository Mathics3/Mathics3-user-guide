PixelValue
==========

`WMA link <https://reference.wolfram.com/language/ref/PixelValue.html>`_


:code:`PixelValue` [:math:`image`, {:math:`x`, :math:`y`}]
    gives the value of the pixel at position {:math:`x`, :math:`y`} in :math:`image`.





>>> hedy = Import["ExampleData/hedy.tif"];

>>> PixelValue[hedy, {1, 1}]
  = {0.439216, 0.356863, 0.337255}
