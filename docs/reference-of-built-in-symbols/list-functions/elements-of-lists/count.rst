Count
=====

`WMA link <https://reference.wolfram.com/language/ref/Count.html>`_


:code:`Count` [:math:`list`, :math:`pattern`]
    returns the number of times :math:`pattern` appears in :math:`list`.

:code:`Count` [:math:`list`, :math:`pattern`, :math:`ls`]
    counts the elements matching at levelspec :math:`ls`.





>>> Count[{3, 7, 10, 7, 5, 3, 7, 10}, 3]
  = 2
>>> Count[{{a, a}, {a, a, a}, a}, a, {2}]
  = 5
