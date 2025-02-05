AssociationQ
============

`WMA link <https://reference.wolfram.com/language/ref/AssociationQ.html>`_


:code:`AssociationQ` [:math:`expr`]
    return True if :math:`expr` is a valid Association object, and False otherwise.





>>> AssociationQ[<|a -> 1, b :> 2|>]
  = True
>>> AssociationQ[<|a, b|>]
  = False
