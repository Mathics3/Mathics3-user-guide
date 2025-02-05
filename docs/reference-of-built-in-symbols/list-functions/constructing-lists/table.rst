Table
=====

`WMA link <https://reference.wolfram.com/language/ref/Table.html>`_


:code:`Table` [:math:`expr`, :math:`n`]
    generates a list of :math:`n` copies of :math:`expr`.

:code:`Table` [:math:`expr`, {:math:`i`, :math:`n`}]
    generates a list of the values of expr when :math:`i` runs from 1 to :math:`n`.

:code:`Table` [:math:`expr`, {:math:`i`, :math:`start`, :math:`stop`, :math:`step`}]
    evaluates :math:`expr` with :math:`i` ranging from :math:`start` to :math:`stop`, incrementing by :math:`step`.

:code:`Table` [:math:`expr`, {:math:`i`, {:math:`e_1`, :math:`e_2`, ..., :math:`ei`}}]
    evaluates :math:`expr` with :math:`i` taking on the values :math:`e_1`, :math:`e_2`, ..., :math:`ei`.





>>> Table[x, 3]
  = {x, x, x}
>>> n = 0; Table[n = n + 1, {5}]
  = {1, 2, 3, 4, 5}
>>> Clear[n]

>>> Table[i, {i, 4}]
  = {1, 2, 3, 4}
>>> Table[i, {i, 2, 5}]
  = {2, 3, 4, 5}
>>> Table[i, {i, 2, 6, 2}]
  = {2, 4, 6}
>>> Table[i, {i, Pi, 2 Pi, Pi / 2}]
  = {Pi, 3 Pi / 2, 2 Pi}
>>> Table[x^2, {x, {a, b, c}}]
  = {a ^ 2, b ^ 2, c ^ 2}

:code:`Table`  supports multi-dimensional tables:

>>> Table[{i, j}, {i, {a, b}}, {j, 1, 2}]
  = {{{a, 1}, {a, 2}}, {{b, 1}, {b, 2}}}

Symbolic bounds:

>>> Table[x, {x, a, a + 5 n, n}]
  = {a, a + n, a + 2 n, a + 3 n, a + 4 n, a + 5 n}

The lower bound is always included even for large step sizes:

>>> Table[i, {i, 1, 9, Infinity}]
  = {1}
