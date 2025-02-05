PadRight
========

`WMA link <https://reference.wolfram.com/language/ref/PadRight.html>`_


:code:`PadRight` [:math:`list`, :math:`n`]
    pads :math:`list` to length :math:`n` by adding 0 on the right.

:code:`PadRight` [:math:`list`, :math:`n`, :math:`x`]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the right.

:code:`PadRight` [:math:`list`, {:math:`n_1`, :math:`n_2`, ...}, :math:`x`]
    pads :math:`list` to lengths :math:`n_1`, :math:`n_2` at levels 1, 2, ... respectively by adding :math:`x` on the right.

:code:`PadRight` [:math:`list`, :math:`n`, :math:`x`, :math:`m`]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the left and adding a margin of :math:`m` on the left.

:code:`PadRight` [:math:`list`, :math:`n`, :math:`x`, {:math:`m_1`, :math:`m_2`, ...}]
    pads :math:`list` to length :math:`n` by adding :math:`x` on the right and adding margins of :math:`m_1`, :math:`m_2`, ...
    on levels 1, 2, ... on the left.

:code:`PadRight` [:math:`list`]
    turns the ragged list :math:`list` into a regular list by adding 0 on the right.





>>> PadRight[{1, 2, 3}, 5]
  = {1, 2, 3, 0, 0}
>>> PadRight[x[a, b, c], 5]
  = x[a, b, c, 0, 0]
>>> PadRight[{1, 2, 3}, 2]
  = {1, 2}
>>> PadRight[{{}, {1, 2}, {1, 2, 3}}]
  = {{0, 0, 0}, {1, 2, 0}, {1, 2, 3}}
>>> PadRight[{1, 2, 3}, 10, {a, b, c}, 2]
  = {b, c, 1, 2, 3, a, b, c, a, b}
>>> PadRight[{{1, 2, 3}}, {5, 2}, x, 1]
  = {{x, x}, {x, 1}, {x, x}, {x, x}, {x, x}}
