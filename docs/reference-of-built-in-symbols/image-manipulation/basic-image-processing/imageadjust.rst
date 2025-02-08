ImageAdjust
===========

`WMA link <https://reference.wolfram.com/language/ref/ImageAdjust.html>`_


:code:`ImageAdjust` [:math:`image`]
    adjusts the levels in :math:`image`.

:code:`ImageAdjust` [:math:`image`, :math:`c`]
    adjusts the contrast in :math:`image` by :math:`c`.

:code:`ImageAdjust` [:math:`image`, {:math:`c`, :math:`b`}]
    adjusts the contrast :math:`c`, and brightness :math:`b` in :math:`image`.

:code:`ImageAdjust` [:math:`image`, {:math:`c`, :math:`b`, :math:`g`}]
    adjusts the contrast :math:`c`, brightness :math:`b`, and gamma :math:`g` in :math:`image`.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> ImageAdjust[hedy]
    =

.. image:: tmpw1_ye1as.png
    :align: center



