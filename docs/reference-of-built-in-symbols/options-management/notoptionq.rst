NotOptionQ
==========

`WMA link <https://reference.wolfram.com/language/ref/NotOptionQ.html>`_


:code:`NotOptionQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` does not have the form of a valid           option specification.





>>> NotOptionQ[x]
  = True
>>> NotOptionQ[2]
  = True
>>> NotOptionQ["abc"]
  = True
>>> NotOptionQ[a -> True]
  = False
