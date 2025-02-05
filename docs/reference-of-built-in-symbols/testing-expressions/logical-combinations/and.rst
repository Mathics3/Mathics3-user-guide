And
===

`WMA link <https://reference.wolfram.com/language/ref/And.html>`_


:code:`And` [:math:`expr_1`, :math:`expr_2`, ...]
    same as

:code:`:math:`expr_1` && :math:`expr_2` && ...`
    evaluates each expression in turn, returning :code:`False`            as soon as an expression evaluates to :code:`False` . If all           expressions evaluate to :code:`True` , :code:`And`  returns :code:`True` .





>>> True && True && False
  = False

If an expression does not evaluate to :code:`True`  or :code:`False` , :code:`And`      returns a result in symbolic form:

>>> a && b && True && c
  = a && b && c
