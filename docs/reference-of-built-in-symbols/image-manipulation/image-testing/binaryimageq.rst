BinaryImageQ
============

`WMA link <https://reference.wolfram.com/language/ref/BinaryImageQ.html>`_


:code:`BinaryImageQ` [:math:`image`]
    returns :code:`True`  if the pixels of :math:`image` are binary bit values, and :code:`False`  otherwise.





>>> img = Import["ExampleData/hedy.tif"];


>>> BinaryImageQ[img]

    =
:math:`\text{False}`


>>> BinaryImageQ[Binarize[img]]

    =
:math:`\text{True}`


