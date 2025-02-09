Sharpen
=======

`WMA link <https://reference.wolfram.com/language/ref/Sharpen.html>`_


:code:`Sharpen` [:math:`image`]
    gives a sharpened version of :math:`image`.

:code:`Sharpen` [:math:`image`, :math:`r`]
    sharpens :math:`image` with a kernel of size :math:`r`.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> Sharpen[hedy]

    =
.. image:: tmponms0ikn.png
    :align: center



>>> Sharpen[hedy, 5]

    =
.. image:: tmp0r9i2tux.png
    :align: center



