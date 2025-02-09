Equivalent
==========

`WMA link <https://reference.wolfram.com/language/ref/Equivalent.html>`_


:code:`Equivalent` [:math:`expr_1`, :math:`expr_2`, ...]
    same as

:math:`expr_1` ⧦ :math:`expr_2` ⧦ ...
    is equivalent to
    (:math:`expr_1` && :math:`expr_2` && ...) || (!:math:`expr_1` && !:math:`expr_2` && ...)





>>> Equivalent[True, True, False]

    =
:math:`\text{False}`



If all expressions do not evaluate to :code:`True`  or :code:`False` , :code:`Equivalent`      returns a result in symbolic form:

>>> Equivalent[a, b, c]

    =
:math:`a\text{$\backslash$[Equivalent]}b\text{$\backslash$[Equivalent]}c`



Otherwise, :code:`Equivalent`  returns a result in DNF

>>> Equivalent[a, b, True, c]

    =
:math:`a\text{\&\&}b\text{\&\&}c`


