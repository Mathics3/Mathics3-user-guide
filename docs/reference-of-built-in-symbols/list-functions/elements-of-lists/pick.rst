Pick
====

`WMA link <https://reference.wolfram.com/language/ref/Pick.html>`_


:code:`Pick` [:math:`list`, :math:`sel`]
    returns those items in :math:`list` that are True in :math:`sel`.

:code:`Pick` [:math:`list`, :math:`sel`, :math:`patt`]
    returns those items in :math:`list` that match :math:`patt` in :math:`sel`.





>>> Pick[{a, b, c}, {False, True, False}]
  = {b}
>>> Pick[f[g[1, 2], h[3, 4]], {{True, False}, {False, True}}]
  = f[g[1], h[4]]
>>> Pick[{a, b, c, d, e}, {1, 2, 3.5, 4, 5.5}, _Integer]
  = {a, b, d}
