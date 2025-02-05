Or
==

`WMA link <https://reference.wolfram.com/language/ref/Or.html>`_


:code:`Or` [:math:`expr_1`, :math:`expr_2`, ...]
    same as

:code:`:math:`expr_1` || :math:`expr_2` || ...`
    evaluates each expression in turn, returning :code:`True`
    as soon as an expression evaluates to :code:`True` . If all
    expressions evaluate to :code:`False` , :code:`Or`  returns :code:`False` .





>>> False || True
  = True

If an expression does not evaluate to :code:`True`  or :code:`False` , :code:`Or` 
returns a result in symbolic form:

>>> a || False || b
  = a || b
