ImageAspectRatio
================

`WMA link <https://reference.wolfram.com/language/ref/ImageAspectRatio.html>`_


:code:`ImageAspectRatio` [:math:`image`]
    gives the aspect ratio of :math:`image`.





>>> img = Import["ExampleData/hedy.tif"];

>>> ImageAspectRatio[img]
  = 400 / 323
>>> ImageAspectRatio[Image[{{0, 1}, {1, 0}, {1, 1}}]]
  = 3 / 2
