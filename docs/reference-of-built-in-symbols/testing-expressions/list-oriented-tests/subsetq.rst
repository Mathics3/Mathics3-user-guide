SubsetQ
=======

`WMA link <https://reference.wolfram.com/language/ref/SubsetQ.html>`_


:code:`SubsetQ` [:math:`list_1`, :math:`list_2`]
    returns True if :math:`list_2` is a subset of :math:`list_1`, and False otherwise.





>>> SubsetQ[{1, 2, 3}, {3, 1}]

    =
:math:`\text{True}`



The empty list is a subset of every list:

>>> SubsetQ[{}, {}]

    =
:math:`\text{True}`


>>> SubsetQ[{1, 2, 3}, {}]

    =
:math:`\text{True}`



Every list is a subset of itself:

>>> SubsetQ[{1, 2, 3}, {1, 2, 3}]

    =
:math:`\text{True}`


