Limit
=====

`WMA link <https://reference.wolfram.com/language/ref/Limit.html>`_


:code:`Limit` [:math:`expr`, :math:`x`->:math:`x_0`]
    gives the limit of :math:`expr` as :math:`x` approaches :math:`x_0`.

:code:`Limit` [:math:`expr`, :math:`x`->:math:`x_0`, Direction->1]
    approaches :math:`x_0` from smaller values.

:code:`Limit` [:math:`expr`, :math:`x`->:math:`x_0`, Direction->-1]
    approaches :math:`x_0` from larger values.





>>> Limit[x, x->2]

    =
:math:`2`


>>> Limit[Sin[x] / x, x->0]

    =
:math:`1`


>>> Limit[1/x, x->0, Direction->-1]

    =
:math:`\infty`


>>> Limit[1/x, x->0, Direction->1]

    =
:math:`-\infty`


