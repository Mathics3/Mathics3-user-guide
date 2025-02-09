ImageChannels
=============

`WMA link <https://reference.wolfram.com/language/ref/ImageChannels.html>`_


:code:`ImageChannels` [:math:`image`]
    gives the number of channels in :math:`image`.





>>> ImageChannels[Image[{{0, 1}, {1, 0}}]]

    =
:math:`1`


>>> img = Import["ExampleData/hedy.tif"];


>>> ImageChannels[img]

    =
:math:`3`


