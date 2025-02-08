PixelValuePositions
===================

`WMA link <https://reference.wolfram.com/language/ref/PixelValuePositions.html>`_


:code:`PixelValuePositions` [:math:`image`, :math:`val`]
    gives the positions of all pixels in :math:`image` that have value :math:`val`.





>>> PixelValuePositions[Image[{{0, 1}, {1, 0}, {1, 1}}], 1]
    =

:math:`\left\{\left\{1,1\right\},\left\{1,2\right\},\left\{2,1\right\},\left\{2,3\right\}\right\}`


>>> PixelValuePositions[Image[{{0.2, 0.4}, {0.9, 0.6}, {0.3, 0.8}}], 0.5, 0.15]
    =

:math:`\left\{\left\{2,2\right\},\left\{2,3\right\}\right\}`


>>> hedy = Import["ExampleData/hedy.tif"];


>>> PixelValuePositions[hedy, 1, 0][[1]]
    =

:math:`\left\{101,491,1\right\}`


>>> PixelValue[hedy, {180, 192}]
    =

:math:`\left\{0.00784314,0.00784314,0.0156863\right\}`


