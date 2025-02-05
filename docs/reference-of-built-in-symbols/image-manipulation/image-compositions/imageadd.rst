ImageAdd
========

`WMA link <https://reference.wolfram.com/language/ref/ImageAdd.html>`_


:code:`ImageAdd` [:math:`image`, :math:`expr_1`, :math:`expr_2`, ...]
    adds all :math:`expr_i` to :math:`image` where each :math:`expr_i` must be an image           or a real number.





>>> i = Image[{{0, 0.5, 0.2, 0.1, 0.9}, {1.0, 0.1, 0.3, 0.8, 0.6}}];

>>> ImageAdd[i, 0.5]
  = -Image-
>>> ImageAdd[i, i]
  = -Image-
>>> ein = Import["ExampleData/Einstein.jpg"];

>>> noise = RandomImage[{-0.1, 0.1}, ImageDimensions[ein]];

>>> ImageAdd[noise, ein]
  = -Image-
>>> hedy = Import["ExampleData/hedy.tif"];

>>> noise = RandomImage[{-0.2, 0.2}, ImageDimensions[hedy], ColorSpace -> "RGB"];

>>> ImageAdd[noise, hedy]
  = -Image-
