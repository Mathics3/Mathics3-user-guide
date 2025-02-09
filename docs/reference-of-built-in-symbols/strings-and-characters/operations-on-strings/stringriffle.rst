StringRiffle
============

`WMA link <https://reference.wolfram.com/language/ref/StringRiffle.html>`_


:code:`StringRiffle[{s1, s2, s3, ...}]`
    returns a new string by concatenating all the :math:`si`, with spaces inserted between them.

:code:`StringRiffle[list, sep]`
    inserts the separator :math:`sep` between all elements in :math:`list`.

:code:`StringRiffle[list, {"left", "sep", "right"}]`
    use :math:`left` and :math:`right` as delimiters after concatenation.





>>> StringRiffle[{"a", "b", "c", "d", "e"}]

    =
:math:`\text{a b c d e}`


>>> StringRiffle[{"a", "b", "c", "d", "e"}, ", "]

    =
:math:`\text{a, b, c, d, e}`


>>> StringRiffle[{"a", "b", "c", "d", "e"}, {"(", " ", ")"}]

    =
:math:`\text{(a b c d e)}`


