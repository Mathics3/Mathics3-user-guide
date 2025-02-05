Join
====

`WMA link <https://reference.wolfram.com/language/ref/Join.html>`_


:code:`Join` [:math:`l_1`, :math:`l_2`]
    concatenates the lists :math:`l_1` and :math:`l_2`.





:code:`Join`  concatenates lists:

>>> Join[{a, b}, {c, d, e}]
  = {a, b, c, d, e}
>>> Join[{{a, b}, {c, d}}, {{1, 2}, {3, 4}}]
  = {{a, b}, {c, d}, {1, 2}, {3, 4}}

The concatenated expressions may have any head:

>>> Join[a + b, c + d, e + f]
  = a + b + c + d + e + f

However, it must be the same for all expressions:

>>> Join[a + b, c * d]
  = Join[a + b, c d]
