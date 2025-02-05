PatternsOrderedQ
================


:code:`PatternsOrderedQ` [:math:`patt1`, :math:`patt2`]
    returns :code:`True`  if pattern :math:`patt1` would be applied before
    :math:`patt2` according to canonical pattern ordering.





>>> PatternsOrderedQ[x__, x_]
  = False
>>> PatternsOrderedQ[x_, x__]
  = True
>>> PatternsOrderedQ[b, a]
  = True
