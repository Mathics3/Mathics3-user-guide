Complement
==========

`WMA link <https://reference.wolfram.com/language/ref/Complement.html>`_


:code:`Complement` [:math:`all`, :math:`e_1`, :math:`e_2`, ...]
    returns an expression containing the elements in the set :math:`all`           that are not in any of :math:`e_1`, :math:`e_2`, etc.

:code:`Complement` [:math:`all`, :math:`e_1`, :math:`e_2`, ..., SameTest->:math:`test`]
    applies :math:`test` to the elements in :math:`all` and each of the :math:`ei` to           determine equality.





The sets :math:`all`, :math:`e_1`, etc can have any head, which must all match.

The returned expression has the same head as the input     expressions. The expression will be sorted and each element will     only occur once.

>>> Complement[{a, b, c}, {a, c}]
  = {b}
>>> Complement[{a, b, c}, {a, c}, {b}]
  = {}
>>> Complement[f[z, y, x, w], f[x], f[x, z]]
  = f[w, y]
>>> Complement[{c, b, a}]
  = {a, b, c}
