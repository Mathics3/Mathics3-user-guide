Root
====

`WMA link <https://reference.wolfram.com/language/ref/Root.html>`_


:code:`Root` [:math:`f`, :math:`i`]
    represents the i-th complex root of the polynomial :math:`f`.





>>> Root[#1 ^ 2 - 1&, 1]

    =
:math:`-1`


>>> Root[#1 ^ 2 - 1&, 2]

    =
:math:`1`



Roots that can't be represented by radicals:

>>> Root[#1 ^ 5 + 2 #1 + 1&, 2]

    =
:math:`\text{Root}\left[1+\text{\#1}^5+2 \text{\#1}\&,2\right]`


