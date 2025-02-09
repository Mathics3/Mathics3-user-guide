Implies
=======

`WMA link <https://reference.wolfram.com/language/ref/Implies.html>`_


:code:`Implies` [:math:`expr_1`, :math:`expr_2`]
    same as

:math:`expr_1` ⇒ :math:`expr_2`
    evaluates each expression in turn, returning :code:`True`          as soon as the first expression evaluates to :code:`False` . If the         first expression evaluates to :code:`True` , :code:`Implies`  returns the         second expression.





>>> Implies[False, a]

    =
:math:`\text{True}`


>>> Implies[True, a]

    =
:math:`a`



If an expression does not evaluate to :code:`True`  or :code:`False` , :code:`Implies` 
returns a result in symbolic form:

>>> Implies[a, Implies[b, Implies[True, c]]]

    =
:math:`a\text{Implies}b\text{Implies}c`


