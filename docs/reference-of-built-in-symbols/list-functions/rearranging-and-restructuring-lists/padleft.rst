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
    =

:math:`\left\{0,0,1,2,3\right\}`


>>> PadLeft[x[a, b, c], 5]
    =

:math:`x\left[0,0,a,b,c\right]`


>>> PadLeft[{1, 2, 3}, 2]
    =

:math:`\left\{2,3\right\}`


>>> PadLeft[{{}, {1, 2}, {1, 2, 3}}]
    =

:math:`\left\{\left\{0,0,0\right\},\left\{0,1,2\right\},\left\{1,2,3\right\}\right\}`


>>> PadLeft[{1, 2, 3}, 10, {a, b, c}, 2]
    =

:math:`\left\{b,c,a,b,c,1,2,3,a,b\right\}`


>>> PadLeft[{{1, 2, 3}}, {5, 2}, x, 1]
    =

:math:`\left\{\left\{x,x\right\},\left\{x,x\right\},\left\{x,x\right\},\left\{3,x\right\},\left\{x,x\right\}\right\}`


