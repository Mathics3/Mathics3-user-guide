Xor
===

`WMA link <https://reference.wolfram.com/language/ref/Xor.html>`_


:code:`Xor` [:math:`expr_1`, :math:`expr_2`, ...]
    same as

:math:`expr_1` ⊻ :math:`expr_2` ⊻ ...
    evaluates each expression in turn, returning :code:`True`
    as soon as not all expressions evaluate to the same value. If all
    expressions evaluate to the same value, :code:`Xor`  returns :code:`False` .





>>> Xor[False, True]

    =
:math:`\text{True}`


>>> Xor[True, True]

    =
:math:`\text{False}`



If an expression does not evaluate to :code:`True`  or :code:`False` , :code:`Xor` 
returns a result in symbolic form:

>>> Xor[a, False, b]

    =
:math:`a\text{$\backslash$[Xor]}b`


