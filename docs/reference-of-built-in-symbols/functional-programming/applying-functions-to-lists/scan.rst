Scan
====

`WMA link <https://reference.wolfram.com/language/ref/Scan.html>`_


:code:`Scan` [:math:`f`, :math:`expr`]
    applies :math:`f` to each element of :math:`expr` and returns :code:`Null` .

:code:`Scan` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` to each level specified by :math:`levelspec` of :math:`expr`.





>>> Scan[Print, {1, 2, 3}]

