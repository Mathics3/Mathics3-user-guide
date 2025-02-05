Insert
======

`WMA link <https://reference.wolfram.com/language/ref/Insert.html>`_


:code:`Insert` [:math:`list`, :math:`elem`, :math:`n`]
    inserts :math:`elem` at position :math:`n` in :math:`list`. When :math:`n` is negative,           the position is counted from the end.





>>> Insert[{a,b,c,d,e}, x, 3]
  = {a, b, x, c, d, e}
>>> Insert[{a,b,c,d,e}, x, -2]
  = {a, b, c, d, x, e}
