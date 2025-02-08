Partition
=========

`WMA link <https://reference.wolfram.com/language/ref/Partition.html>`_


:code:`Partition` [:math:`list`, :math:`n`]
    partitions :math:`list` into sublists of length :math:`n`.

:code:`Partition` [:math:`list`, :math:`n`, :math:`d`]
    partitions :math:`list` into sublists of length :math:`n` which overlap :math:`d`           indices.





>>> Partition[{a, b, c, d, e, f}, 2]
    =

:math:`\left\{\left\{a,b\right\},\left\{c,d\right\},\left\{e,f\right\}\right\}`


>>> Partition[{a, b, c, d, e, f}, 3, 1]
    =

:math:`\left\{\left\{a,b,c\right\},\left\{b,c,d\right\},\left\{c,d,e\right\},\left\{d,e,f\right\}\right\}`


