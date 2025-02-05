Partition
=========

`WMA link <https://reference.wolfram.com/language/ref/Partition.html>`_


:code:`Partition` [:math:`list`, :math:`n`]
    partitions :math:`list` into sublists of length :math:`n`.

:code:`Partition` [:math:`list`, :math:`n`, :math:`d`]
    partitions :math:`list` into sublists of length :math:`n` which overlap :math:`d`           indices.





>>> Partition[{a, b, c, d, e, f}, 2]
  = {{a, b}, {c, d}, {e, f}}
>>> Partition[{a, b, c, d, e, f}, 3, 1]
  = {{a, b, c}, {b, c, d}, {c, d, e}, {d, e, f}}
