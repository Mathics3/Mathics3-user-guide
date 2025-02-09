ImageData
=========

`WMA link <https://reference.wolfram.com/language/ref/ImageData.html>`_


:code:`ImageData` [:math:`image`]
    gives a list of all color values of :math:`image` as a matrix.

:code:`ImageData` [:math:`image`, :math:`stype`]
    gives a list of color values in type :math:`stype`.





>>> img = Image[{{0.2, 0.4}, {0.9, 0.6}, {0.5, 0.8}}];


>>> ImageData[img]

    =
:math:`\left\{\left\{0.2,0.4\right\},\left\{0.9,0.6\right\},\left\{0.5,0.8\right\}\right\}`


>>> ImageData[img, "Byte"]

    =
:math:`\left\{\left\{51,102\right\},\left\{229,153\right\},\left\{127,204\right\}\right\}`


>>> ImageData[Image[{{0, 1}, {1, 0}, {1, 1}}], "Bit"]

    =
:math:`\left\{\left\{0,1\right\},\left\{1,0\right\},\left\{1,1\right\}\right\}`


