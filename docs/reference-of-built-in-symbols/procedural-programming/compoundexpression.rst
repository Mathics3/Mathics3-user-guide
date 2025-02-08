CompoundExpression
==================

`WMA link <https://reference.wolfram.com/language/ref/CompoundExpression.html>`_


:code:`CompoundExpression` [:math:`e_1`, :math:`e_2`, ...]
    same as

:math:`e_1`:code:`;`  :math:`e_2`:code:`;`  ...
    evaluates its arguments in turn, returning the last result.





>>> a; b; c; d
    =

:math:`d`



If the last argument is omitted, :code:`Null`  is taken:

>>> a;


