HammingDistance
===============

`WMA link <https://reference.wolfram.com/language/ref/HammingDistance.html>`_


:code:`HammingDistance` [:math:`u`, :math:`v`]
    returns the Hamming distance between :math:`u` and :math:`v`, i.e. the number of different elements.
    :math:`u` and :math:`v` may be lists or strings.





>>> HammingDistance[{1, 0, 1, 0}, {1, 0, 0, 1}]

    =
:math:`2`


>>> HammingDistance["time", "dime"]

    =
:math:`1`


>>> HammingDistance["TIME", "dime", IgnoreCase -> True]

    =
:math:`1`


