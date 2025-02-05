SparseArray
===========

`WMA link <https://reference.wolfram.com/language/ref/SparseArray.html>`_


:code:`SparseArray` [:math:`rules`]
    Builds a sparse array according to the list of :math:`rules`.

:code:`SparseArray` [:math:`rules`, :math:`dims`]
    Builds a sparse array of dimensions :math:`dims` according to the :math:`rules`.

:code:`SparseArray` [:math:`list`]
    Builds a sparse representation of :math:`list`.





>>> SparseArray[{{1, 2} -> 1, {2, 1} -> 1}]
  = SparseArray[Automatic, {2, 2}, 0, {{1, 2} -> 1, {2, 1} -> 1}]
>>> SparseArray[{{1, 2} -> 1, {2, 1} -> 1}, {3, 3}]
  = SparseArray[Automatic, {3, 3}, 0, {{1, 2} -> 1, {2, 1} -> 1}]
>>> M=SparseArray[{{0, a}, {b, 0}}]
  = SparseArray[Automatic, {2, 2}, 0, {{1, 2} -> a, {2, 1} -> b}]
>>> M //Normal
  = {{0, a}, {b, 0}}
