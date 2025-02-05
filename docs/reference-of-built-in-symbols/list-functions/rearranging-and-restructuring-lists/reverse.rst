Reverse
=======

`WMA link <https://reference.wolfram.com/language/ref/Reverse.html>`_


:code:`Reverse` [:math:`expr`]
    reverses the order of :math:`expr`'s items (on the top level)

:code:`Reverse` [:math:`expr`, :math:`n`]
    reverses the order of items in :math:`expr` on level :math:`n`

:code:`Reverse` [:math:`expr`, {:math:`n_1`, :math:`n_2`, ...}]
    reverses the order of items in :math:`expr` on levels :math:`n_1`, :math:`n_2`, ...





>>> Reverse[{1, 2, 3}]
  = {3, 2, 1}
>>> Reverse[x[a, b, c]]
  = x[c, b, a]
>>> Reverse[{{1, 2}, {3, 4}}, 1]
  = {{3, 4}, {1, 2}}
>>> Reverse[{{1, 2}, {3, 4}}, 2]
  = {{2, 1}, {4, 3}}
>>> Reverse[{{1, 2}, {3, 4}}, {1, 2}]
  = {{4, 3}, {2, 1}}
