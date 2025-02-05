MapThread
=========

`WMA link <https://reference.wolfram.com/language/ref/MapThread.html>`_


'MapThread[:math:`f`, {{:math:`a_1`, :math:`a_2`, ...}, {:math:`b_1`, :math:`b_2`, ...}, ...}]
    returns :code:`{:math:`f`[:math:`a_1`, :math:`b_1`, ...], :math:`f`[:math:`a_2`, :math:`b_2`, ...], ...}` .

:code:`MapThread` [:math:`f`, {:math:`expr_1`, :math:`expr_2`, ...}, :math:`n`]
    applies :math:`f` at level :math:`n`.





>>> MapThread[f, {{a, b, c}, {1, 2, 3}}]
  = {f[a, 1], f[b, 2], f[c, 3]}
>>> MapThread[f, {{{a, b}, {c, d}}, {{e, f}, {g, h}}}, 2]
  = {{f[a, e], f[b, f]}, {f[c, g], f[d, h]}}
