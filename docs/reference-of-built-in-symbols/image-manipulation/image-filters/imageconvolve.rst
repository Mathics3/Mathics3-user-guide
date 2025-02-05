ImageConvolve
=============

`WMA link <https://reference.wolfram.com/language/ref/ImageConvolve.html>`_


:code:`ImageConvolve` [:math:`image`, :math:`kernel`]
    Computes the convolution of :math:`image` using :math:`kernel`.





>>> hedy = Import["ExampleData/hedy.tif"];

>>> ImageConvolve[hedy, DiamondMatrix[5] / 61]
  = -Image-
>>> ImageConvolve[hedy, DiskMatrix[5] / 97]
  = -Image-
>>> ImageConvolve[hedy, BoxMatrix[5] / 121]
  = -Image-
