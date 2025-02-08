QuantityMagnitude
=================

`WMA link <https://reference.wolfram.com/language/ref/QuantityMagnitude.html>`_


:code:`QuantityMagnitude` [:math:`quantity`]
    gives the amount of the specified :math:`quantity`.

:code:`QuantityMagnitude` [:math:`quantity`, :math:`unit`]
    gives the value corresponding to :math:`quantity` when converted to :math:`unit`.





>>> QuantityMagnitude[Quantity["Kilogram"]]
    =

:math:`1`


>>> QuantityMagnitude[Quantity[10, "Meters"]]
    =

:math:`10`


>>> QuantityMagnitude[Quantity[{10,20}, "Meters"]]
    =

:math:`\left\{10,20\right\}`


