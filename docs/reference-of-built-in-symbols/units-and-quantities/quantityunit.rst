QuantityUnit
============

`WMA link <https://reference.wolfram.com/language/ref/QuantityUnit.html>`_


:code:`QuantityUnit` [:math:`quantity`]
    returns the unit associated with the specified :math:`quantity`.





>>> QuantityUnit[Quantity["Kilogram"]]

    =
:math:`\text{kilogram}`


>>> QuantityUnit[Quantity[10, "Meters"]]

    =
:math:`\text{meter}`


>>> QuantityUnit[Quantity[{10,20}, "Meters"]]

    =
:math:`\left\{\text{meter},\text{meter}\right\}`


