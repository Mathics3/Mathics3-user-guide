Tuples
======

`WMA link <https://reference.wolfram.com/language/ref/Tuples.html>`_


:code:`Tuples` [:math:`list`, :math:`n`]
    returns a list of all :math:`n`-tuples of elements in :math:`list`.

:code:`Tuples` [{:math:`list_1`, :math:`list_2`, ...}]
    returns a list of tuples with elements from the given lists.





>>> Tuples[{a, b, c}, 2]
  = {{a, a}, {a, b}, {a, c}, {b, a}, {b, b}, {b, c}, {c, a}, {c, b}, {c, c}}
>>> Tuples[{}, 2]
  = {}
>>> Tuples[{a, b, c}, 0]
  = {{}}
>>> Tuples[{{a, b}, {1, 2, 3}}]
  = {{a, 1}, {a, 2}, {a, 3}, {b, 1}, {b, 2}, {b, 3}}

The head of :math:`list` need not be :code:`List` :

>>> Tuples[f[a, b, c], 2]
  = {f[a, a], f[a, b], f[a, c], f[b, a], f[b, b], f[b, c], f[c, a], f[c, b], f[c, c]}

However, when specifying multiple expressions, :code:`List`  is always used:

>>> Tuples[{f[a, b], g[c, d]}]
  = {{a, c}, {a, d}, {b, c}, {b, d}}
