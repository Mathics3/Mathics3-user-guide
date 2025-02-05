Opening
=======

`WMA link <https://reference.wolfram.com/language/ref/Opening.html>`_


:code:`Opening` [:math:`image`, :math:`ker`]
    Gives the morphological opening of :math:`image` with respect to structuring element :math:`ker`.





>>> ein = Import["ExampleData/Einstein.jpg"];

>>> Opening[ein, 2.5]
  = -Image-
