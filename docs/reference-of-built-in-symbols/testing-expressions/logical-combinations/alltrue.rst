AllTrue
=======

`WMA link <https://reference.wolfram.com/language/ref/AllTrue.html>`_


:code:`AllTrue` [{:math:`expr_1`, :math:`expr_2`, ...}, :math:`test`]
    returns True if all applications of :math:`test` to :math:`expr_1`, :math:`expr_2`, ... evaluate to True.

:code:`AllTrue` [:math:`list`, :math:`test`, :math:`level`]
    returns True if all applications of :math:`test` to items of :math:`list` at :math:`level` evaluate to True.

:code:`AllTrue` [:math:`test`]
    gives an operator that may be applied to expressions.





>>> AllTrue[{2, 4, 6}, EvenQ]
  = True
>>> AllTrue[{2, 4, 7}, EvenQ]
  = False
