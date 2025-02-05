Rule
====

`WMA link <https://reference.wolfram.com/language/ref/Rule_.html>`_


:code:`Rule` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` -> :math:`y``
    represents a rule replacing :math:`x` with :math:`y`.





>>> a+b+c /. c->d
  = a + b + d
>>> {x,x^2,y} /. x->3
  = {3, 9, y}
>>> a /. Rule[1, 2, 3] -> t
  = a
