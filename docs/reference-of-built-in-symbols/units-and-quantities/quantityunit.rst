QuantityUnit
============

`WMA link <https://reference.wolfram.com/language/ref/QuantityUnit.html>`_


:code:`QuantityUnit` [:math:`quantity`]
    returns the unit associated with the specified :math:`quantity`.





>>> QuantityUnit[Quantity["Kilogram"]]
  = kilogram
>>> QuantityUnit[Quantity[10, "Meters"]]
  = meter
>>> QuantityUnit[Quantity[{10,20}, "Meters"]]
  = {meter, meter}
