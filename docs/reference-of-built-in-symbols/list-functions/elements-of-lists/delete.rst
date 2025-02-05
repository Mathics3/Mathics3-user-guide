Delete
======

`WMA link <https://reference.wolfram.com/language/ref/Delete.html>`_


:code:`Delete` [:math:`expr`, :math:`i`]
    deletes the element at position :math:`i` in :math:`expr`. The position is counted from the end if :math:`i` is negative.

:code:`Delete` [:math:`expr`, {:math:`m`, :math:`n`, ...}]
    deletes the element at position {:math:`m`, :math:`n`, ...}.

:code:`Delete` [:math:`expr`, {{:math:`m_1`, :math:`n_1`, ...}, {:math:`m_2`, :math:`n_2`, ...}, ...}]
    deletes the elements at several positions.





Delete the element at position 3:

>>> Delete[{a, b, c, d}, 3]
  = {a, b, d}

Delete at position 2 from the end:

>>> Delete[{a, b, c, d}, -2]
  = {a, b, d}

Delete at positions 1 and 3:

>>> Delete[{a, b, c, d}, {{1}, {3}}]
  = {b, d}

Delete in a 2D array:

>>> Delete[{{a, b}, {c, d}}, {2, 1}]
  = {{a, b}, {d}}

Deleting the head of a whole expression gives a Sequence object:

>>> Delete[{a, b, c}, 0]
  = Sequence[a, b, c]

Delete in an expression with any head:

>>> Delete[f[a, b, c, d], 3]
  = f[a, b, d]

Delete a head to splice in its arguments:

>>> Delete[f[a, b, u + v, c], {3, 0}]
  = f[a, b, u, v, c]
>>> Delete[{a, b, c}, 0]
  = Sequence[a, b, c]

Delete without the position:

>>> Delete[{a, b, c, d}]
  = Delete[{a, b, c, d}]

Delete with many arguments:

>>> Delete[{a, b, c, d}, 1, 2]
  = Delete[{a, b, c, d}, 1, 2]

Delete the element out of range:

>>> Delete[{a, b, c, d}, 5]
  = Delete[{a, b, c, d}, 5]
>>> Delete[{a, b, c, d}, {1, 2}]
  = Delete[{a, b, c, d}, {1, 2}]

Delete the position not integer:

>>> Delete[{a, b, c, d}, {1, n}]
  = Delete[{a, b, c, d}, {1, n}]
