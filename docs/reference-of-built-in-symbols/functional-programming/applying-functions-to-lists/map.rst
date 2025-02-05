Map
===

`WMA link <https://reference.wolfram.com/language/ref/Map.html>`_


:code:`Map` [:math:`f`, :math:`expr`] or :code:`:math:`f` /@ :math:`expr``
    applies :math:`f` to each part on the first level of :math:`expr`.

:code:`Map` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` to each level specified by :math:`levelspec` of :math:`expr`.





>>> f /@ {1, 2, 3}
  = {f[1], f[2], f[3]}
>>> #^2& /@ {1, 2, 3, 4}
  = {1, 4, 9, 16}

Map :math:`f` on the second level:

>>> Map[f, {{a, b}, {c, d, e}}, {2}]
  = {{f[a], f[b]}, {f[c], f[d], f[e]}}

Include heads:

>>> Map[f, a + b + c, Heads->True]
  = f[Plus][f[a], f[b], f[c]]
