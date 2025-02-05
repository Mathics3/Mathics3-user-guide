QuantityQ
=========

`WMA link <https://reference.wolfram.com/language/ref/QuantityQ.html>`_

:code:`QuantityQ` [:math:`expr`]
    return True if :math:`expr` is a valid Association object, and False otherwise.





>>> QuantityQ[Quantity[3, "Meters"]]
  = True
>>> QuantityQ[Quantity[3, "Maters"]]
  = False
