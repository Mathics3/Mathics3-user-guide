ImagePartition
==============

`WMA link <https://reference.wolfram.com/language/ref/ImagePartition.html>`_


:code:`ImagePartition` [:math:`image`, :math:`s`]
    Partitions an image into an array of :math:`s` x :math:`s` pixel subimages.

:code:`ImagePartition` [:math:`image`, {:math:`w`, :math:`h`}]
    Partitions an image into an array of :math:`w` x :math:`h` pixel subimages.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> ImageDimensions[hedy]

    =
:math:`\left\{646,800\right\}`


>>> ImagePartition[hedy, 256]

>>> ImagePartition[hedy, {512, 128}]

