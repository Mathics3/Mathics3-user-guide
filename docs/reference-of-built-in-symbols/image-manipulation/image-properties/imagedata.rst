ImageData
=========

`WMA link <https://reference.wolfram.com/language/ref/ImageData.html>`_


:code:`ImageData` [:math:`image`]
    gives a list of all color values of :math:`image` as a matrix.

:code:`ImageData` [:math:`image`, :math:`stype`]
    gives a list of color values in type :math:`stype`.





>>> img = Image[{{0.2, 0.4}, {0.9, 0.6}, {0.5, 0.8}}];

>>> ImageData[img]
  = {{0.2, 0.4}, {0.9, 0.6}, {0.5, 0.8}}
>>> ImageData[img, "Byte"]
  = {{51, 102}, {229, 153}, {127, 204}}
>>> ImageData[Image[{{0, 1}, {1, 0}, {1, 1}}], "Bit"]
  = {{0, 1}, {1, 0}, {1, 1}}
