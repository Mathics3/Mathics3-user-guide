PixelValuePositions
===================

`WMA link <https://reference.wolfram.com/language/ref/PixelValuePositions.html>`_


:code:`PixelValuePositions` [:math:`image`, :math:`val`]
    gives the positions of all pixels in :math:`image` that have value :math:`val`.





>>> PixelValuePositions[Image[{{0, 1}, {1, 0}, {1, 1}}], 1]
  = {{1, 1}, {1, 2}, {2, 1}, {2, 3}}
>>> PixelValuePositions[Image[{{0.2, 0.4}, {0.9, 0.6}, {0.3, 0.8}}], 0.5, 0.15]
  = {{2, 2}, {2, 3}}
>>> hedy = Import["ExampleData/hedy.tif"];

>>> PixelValuePositions[hedy, 1, 0][[1]]
  = {101, 491, 1}
>>> PixelValue[hedy, {180, 192}]
  = {0.00784314, 0.00784314, 0.0156863}
