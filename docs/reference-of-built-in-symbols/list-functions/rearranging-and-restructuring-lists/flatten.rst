Flatten
=======

`WMA link <https://reference.wolfram.com/language/ref/Flatten.html>`_


:code:`Flatten` [:math:`expr`]
    flattens out nested lists in :math:`expr`.

:code:`Flatten` [:math:`expr`, :math:`n`]
    stops flattening at level :math:`n`.

:code:`Flatten` [:math:`expr`, :math:`n`, :math:`h`]
    flattens expressions with head :math:`h` instead of :code:`List` .





>>> Flatten[{{a, b}, {c, {d}, e}, {f, {g, h}}}]
  = {a, b, c, d, e, f, g, h}
>>> Flatten[{{a, b}, {c, {e}, e}, {f, {g, h}}}, 1]
  = {a, b, c, {e}, e, f, {g, h}}
>>> Flatten[f[a, f[b, f[c, d]], e], Infinity, f]
  = f[a, b, c, d, e]
>>> Flatten[{{a, b}, {c, d}}, {{2}, {1}}]
  = {{a, c}, {b, d}}
>>> Flatten[{{a, b}, {c, d}}, {{1, 2}}]
  = {a, b, c, d}

Flatten also works in irregularly shaped arrays

>>> Flatten[{{1, 2, 3}, {4}, {6, 7}, {8, 9, 10}}, {{2}, {1}}]
  = {{1, 4, 6, 8}, {2, 7, 9}, {3, 10}}
