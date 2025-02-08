StringTrim
==========

`WMA link <https://reference.wolfram.com/language/ref/StringTrim.html>`_


:code:`StringTrim` [:math:`s`]
    returns a version of :math:`s` with whitespace removed from start and end.





>>> StringJoin["a", StringTrim["  \tb\n "], "c"]
    =

:math:`\text{abc}`


>>> StringTrim["ababaxababyaabab", RegularExpression["(ab)+"]]
    =

:math:`\text{axababya}`


