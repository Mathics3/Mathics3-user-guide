MedianFilter
============

`WMA link <https://reference.wolfram.com/language/ref/MedianFilter.html>`_


:code:`MedianFilter` [:math:`image`, :math:`r`]
    gives :math:`image` with a median filter of radius :math:`r` applied on it. This always           picks the median value in the filter's area.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> MedianFilter[hedy, 5]

    =
.. image:: tmpjvq4dnq7.png
    :align: center



