MaxFilter
=========

`WMA link <https://reference.wolfram.com/language/ref/MaxFilter.html>`_


:code:`MaxFilter` [:math:`image`, :math:`r`]
    gives :math:`image` with a maximum filter of radius :math:`r` applied on it. This always           picks the largest value in the filter's area.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> MaxFilter[hedy, 5]

    =
.. image:: tmpknx6nuww.png
    :align: center



