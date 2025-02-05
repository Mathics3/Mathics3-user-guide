ArrayQ
======

`WMA <https://reference.wolfram.com/language/ref/ArrayQ.html>`_


:code:`ArrayQ` [:math:`expr`]
    tests whether :math:`expr` is a full array.

:code:`ArrayQ` [:math:`expr`, :math:`pattern`]
    also tests whether the array depth of :math:`expr` matches :math:`pattern`.

:code:`ArrayQ` [:math:`expr`, :math:`pattern`, :math:`test`]
    furthermore tests whether :math:`test` yields :code:`True`  for all elements of :math:`expr`.
    :code:`ArrayQ[:math:`expr`]`  is equivalent to :code:`ArrayQ[:math:`expr`, _, True&]` .





>>> ArrayQ[a]
  = False
>>> ArrayQ[{a}]
  = True
>>> ArrayQ[{{{a}},{{b,c}}}]
  = False
>>> ArrayQ[{{a, b}, {c, d}}, 2, SymbolQ]
  = True
