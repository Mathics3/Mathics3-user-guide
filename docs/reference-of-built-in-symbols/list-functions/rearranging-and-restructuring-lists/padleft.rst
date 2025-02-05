PadLeft
=======

`WMA link <https://reference.wolfram.com/language/ref/PadLeft.html>`_


:code:`PadLeft` [:math:`list`, :math:`n`]
    pads :math:`list` to length :math:`n` by adding 0 on the left.

:code:`PadLeft` [:math:`list`, :math:`n`, :math:`x`]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the left.

:code:`PadLeft` [:math:`list`, {:math:`n_1`, :math:`n_2`, ...}, :math:`x`]
    pads :math:`list` to lengths :math:`n_1`, :math:`n_2` at levels 1, 2, ... respectively by adding :math:`x` on the left.

:code:`PadLeft` [:math:`list`, :math:`n`, :math:`x`, :math:`m`]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the left and adding a margin of :math:`m` on the right.

:code:`PadLeft` [:math:`list`, :math:`n`, :math:`x`, {:math:`m_1`, :math:`m_2`, ...}]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the left and adding margins of :math:`m_1`, :math:`m_2`, ...
    on levels 1, 2, ... on the right.

:code:`PadLeft` [:math:`list`]
    turns the ragged list :math:`list` into a regular list by adding 0 on the left.





>>> PadLeft[{1, 2, 3}, 5]
  = {0, 0, 1, 2, 3}
>>> PadLeft[x[a, b, c], 5]
  = x[0, 0, a, b, c]
>>> PadLeft[{1, 2, 3}, 2]
  = {2, 3}
>>> PadLeft[{{}, {1, 2}, {1, 2, 3}}]
  = {{0, 0, 0}, {0, 1, 2}, {1, 2, 3}}
>>> PadLeft[{1, 2, 3}, 10, {a, b, c}, 2]
  = {b, c, a, b, c, 1, 2, 3, a, b}
>>> PadLeft[{{1, 2, 3}}, {5, 2}, x, 1]
  = {{x, x}, {x, x}, {x, x}, {3, x}, {x, x}}
