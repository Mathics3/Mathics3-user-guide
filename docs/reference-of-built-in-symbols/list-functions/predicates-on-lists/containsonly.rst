ContainsOnly
============

`WMA link <https://reference.wolfram.com/language/ref/ContainsOnly.html>`_


:code:`ContainsOnly` [:math:`list_1`, :math:`list_2`]
    yields True if :math:`list_1` contains only elements that appear in :math:`list_2`.





>>> ContainsOnly[{b, a, a}, {a, b, c}]

    =
:math:`\text{True}`



The first list contains elements not present in the second list:

>>> ContainsOnly[{b, a, d}, {a, b, c}]

    =
:math:`\text{False}`


>>> ContainsOnly[{}, {a, b, c}]

    =
:math:`\text{True}`



Use Equal as the comparison function to have numerical tolerance:

>>> ContainsOnly[{a, 1.0}, {1, a, b}, {SameTest -> Equal}]

    =
:math:`\text{True}`


