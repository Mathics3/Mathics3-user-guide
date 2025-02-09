LeafCount
=========

`WMA link <https://reference.wolfram.com/language/ref/LeafCount.html>`_


:code:`LeafCount` [:math:`expr`]
    returns the total number of indivisible subexpressions in :math:`expr`.





>>> LeafCount[1 + x + y^a]

    =
:math:`6`


>>> LeafCount[f[x, y]]

    =
:math:`3`


>>> LeafCount[{1 / 3, 1 + I}]

    =
:math:`7`


>>> LeafCount[Sqrt[2]]

    =
:math:`5`


>>> LeafCount[100!]

    =
:math:`1`


