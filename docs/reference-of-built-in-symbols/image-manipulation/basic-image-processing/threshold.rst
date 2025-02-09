Threshold
=========

`WMA link <https://reference.wolfram.com/language/ref/Threshold.html>`_


:code:`Threshold` [:math:`image`]
    gives a value suitable for binarizing :math:`image`.





The option "Method" may be "Cluster" (use Otsu's threshold), "Median", or "Mean".

>>> img = Import["ExampleData/hedy.tif"];


>>> Threshold[img]

    =
:math:`0.408203`


>>> Binarize[img, %]

    =
.. image:: tmpme5_n00m.png
    :align: center



>>> Threshold[img, Method -> "Mean"]

    =
:math:`0.22086`


>>> Threshold[img, Method -> "Median"]

    =
:math:`0.0593961`


