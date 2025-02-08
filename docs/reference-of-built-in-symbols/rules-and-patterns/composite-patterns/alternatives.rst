Alternatives
============

`WMA link <https://reference.wolfram.com/language/ref/Alternatives.html>`_


:code:`Alternatives` [:math:`p_1`, :math:`p_2`, ..., :math:`p_i`]
    same as

:math:`p_1` :code:`|`  :math:`p_2` :code:`|`  ... :code:`|`  :math:`p_i`
    is a pattern that matches any of the patterns :math:`p_1`, :math:`p_2`,         ...., :math:`p_i`.





>>> a+b+c+d/.(a|b)->t
    =

:math:`c+d+2 t`



Alternatives can also be used for string expressions:

>>> StringReplace["0123 3210", "1" | "2" -> "X"]
    =

:math:`\text{0XX3 3XX0}`


