StringInsert
============

`WMA link <https://reference.wolfram.com/language/ref/StringInsert.html>`_


:code:`StringInsert` [":math:`string`", ":math:`snew`", :math:`n`]
    yields a string with :math:`snew` inserted starting at position :math:`n` in :math:`string`.

:code:`StringInsert` [":math:`string`", ":math:`snew`", -:math:`n`]
    inserts a at position :math:`n` from the end of ":math:`string`".

:code:`StringInsert` [":math:`string`", ":math:`snew`", {:math:`n_1`, :math:`n_2`, ...}]
    inserts a copy of :math:`snew` at each position :math:`n_i` in :math:`string`;
    the :math:`n_i` are taken before any insertion is done.

:code:`StringInsert` [{:math:`s_1`, :math:`s_2`, ...}, ":math:`snew`", :math:`n`]
    gives the list of results for each of the :math:`s_i`.





>>> StringInsert["noting", "h", 4]

    =
:math:`\text{nothing}`


>>> StringInsert["note", "d", -1]

    =
:math:`\text{noted}`


>>> StringInsert["here", "t", -5]

    =
:math:`\text{there}`


>>> StringInsert["adac", "he", {1, 5}]

    =
:math:`\text{headache}`


>>> StringInsert[{"something", "sometimes"}, " ", 5]

    =
:math:`\left\{\text{some thing},\text{some times}\right\}`



Insert dot as millar separators

>>> StringInsert["1234567890123456", ".", Range[-16, -4, 3]]

    =
:math:`\text{1.234.567.890.123.456}`


