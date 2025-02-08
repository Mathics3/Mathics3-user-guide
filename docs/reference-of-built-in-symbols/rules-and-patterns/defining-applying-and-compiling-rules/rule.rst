Rule
====

`WMA link <https://reference.wolfram.com/language/ref/Rule_.html>`_


:code:`Rule` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` -> :math:`y``
    represents a rule replacing :math:`x` with :math:`y`.





>>> a+b+c /. c->d
    =

:math:`a+b+d`


>>> {x,x^2,y} /. x->3
    =

:math:`\left\{3,9,y\right\}`


>>> a /. Rule[1, 2, 3] -> t

    Rule::argrx Rule called with 3 arguments; 2 arguments are expected.
    =

:math:`a`


