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
.. image:: tmp72k0_0h8.png
    :align: center



>>> Blur[hedy, 5]

    =
.. image:: tmp025tvngw.png
    :align: center



