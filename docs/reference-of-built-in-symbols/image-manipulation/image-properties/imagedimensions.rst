ImageDimensions
===============

`WMA link <https://reference.wolfram.com/language/ref/ImageDimensions.html>`_


:code:`ImageDimensions` [:math:`image`]
    Returns the dimensions {:math:`width`, :math:`height`} of :math:`image` in pixels.





>>> hedy = Import["ExampleData/hedy.tif"];

>>> ImageDimensions[hedy]
  = {646, 800}
>>> ImageDimensions[RandomImage[1, {50, 70}]]
  = {50, 70}
