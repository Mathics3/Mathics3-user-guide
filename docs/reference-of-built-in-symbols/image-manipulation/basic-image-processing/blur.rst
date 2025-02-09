Blur
====

`WMA link <https://reference.wolfram.com/language/ref/Blur.html>`_


:code:`Blur` [:math:`image`]
    gives a blurred version of :math:`image`.

:code:`Blur` [:math:`image`, :math:`r`]
    blurs :math:`image` with a kernel of size :math:`r`.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> Blur[hedy]

    =
.. image:: tmpan_mfycl.png
    :align: center



>>> Blur[hedy, 5]

    =
.. image:: tmpo5djuq21.png
    :align: center



