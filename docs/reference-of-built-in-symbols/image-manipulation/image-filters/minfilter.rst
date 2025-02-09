MinFilter
=========

`WMA link <https://reference.wolfram.com/language/ref/MinFilter.html>`_


:code:`MinFilter` [:math:`image`, :math:`r`]
    gives :math:`image` with a minimum filter of radius :math:`r` applied on it. This always           picks the smallest value in the filter's area.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> MinFilter[hedy, 5]

    =
.. image:: tmpirmdb0p1.png
    :align: center



