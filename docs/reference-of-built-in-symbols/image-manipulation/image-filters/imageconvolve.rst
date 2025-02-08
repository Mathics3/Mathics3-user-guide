ImageConvolve
=============

`WMA link <https://reference.wolfram.com/language/ref/ImageConvolve.html>`_


:code:`ImageConvolve` [:math:`image`, :math:`kernel`]
    Computes the convolution of :math:`image` using :math:`kernel`.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> ImageConvolve[hedy, DiamondMatrix[5] / 61]
    =

.. image:: tmpgjaeiyy3.png
    :align: center



>>> ImageConvolve[hedy, DiskMatrix[5] / 97]
    =

.. image:: tmpljimazsj.png
    :align: center



>>> ImageConvolve[hedy, BoxMatrix[5] / 121]
    =

.. image:: tmpu5i7n466.png
    :align: center



