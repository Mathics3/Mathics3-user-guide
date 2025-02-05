Log
===

`WMA link <https://reference.wolfram.com/language/ref/Log.html>`_


:code:`Log` [:math:`z`]
    returns the natural logarithm of :math:`z`.





>>> Log[{0, 1, E, E * E, E ^ 3, E ^ x}]
  = {-Infinity, 0, 1, 2, 3, Log[E ^ x]}
>>> Log[0.]
  = Indeterminate
>>> Plot[Log[x], {x, 0, 5}]
  = -Graphics-
