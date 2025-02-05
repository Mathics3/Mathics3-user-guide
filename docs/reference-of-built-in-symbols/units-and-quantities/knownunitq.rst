KnownUnitQ
==========

`WMA link <https://reference.wolfram.com/language/ref/KnownUnitQ.html>`_


:code:`KnownUnitQ` [:math:`unit`]
    returns True if :math:`unit` is a canonical unit, and False otherwise.





>>> KnownUnitQ["Feet"]
  = True
>>> KnownUnitQ["Foo"]
  = False
>>> KnownUnitQ["meter"^2/"second"]
  = True
