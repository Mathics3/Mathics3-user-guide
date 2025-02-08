Threshold
=========

`WMA link <https://reference.wolfram.com/language/ref/Threshold.html>`_


:code:`Threshold` [:math:`image`]
    gives a value suitable for binarizing :math:`image`.





The option "Method" may be "Cluster" (use Otsu's threshold), "Median", or "Mean".

>>> img = Import["ExampleData/hedy.tif"];


>>> Threshold[img]
    =

:math:`0.0593961`


>>> Binarize[img, %]
    = -Image-`

>>> Threshold[img, Method -> "Mean"]
    = 0.22086`

>>> Threshold[img, Method -> "Median"]
    = 0.0593961`

