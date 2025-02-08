Quantity
========

`WMA link <https://reference.wolfram.com/language/ref/Quantity.html>`_


:code:`Quantity` [:math:`magnitude`, :math:`unit`]
    represents a quantity with size :math:`magnitude` and unit specified by :math:`unit`.

:code:`Quantity` [:math:`unit`]
    assumes the magnitude of the specified :math:`unit` to be 1.





>>> Quantity["Kilogram"]
    =

:math:`1\text{ }\text{kilogram}`


>>> Quantity[10, "Meters"]
    =

:math:`10\text{ }\text{meter}`



If the first argument is an array, then the unit is distributed on each element

>>> Quantity[{10, 20}, "Meters"]
    =

:math:`\left\{10\text{ }\text{meter},20\text{ }\text{meter}\right\}`



If the second argument is a number, then the expression is evaluated to
the product of the magnitude and that number

>>> Quantity[2, 3/2]
    =

:math:`3`



Notice that units are specified as Strings. If the unit is not a Symbol or a Number,
the expression is not interpreted as a Quantity object:

>>> QuantityQ[Quantity[2, Second]]

    Quantity::unkunit Unable to interpret unit specification Second.
    =

:math:`\text{False}`



Quantities can be multiplied and raised to integer powers:

>>> Quantity[3, "centimeter"] / Quantity[2, "second"]^2
    =

:math:`\frac{3}{4}\text{ }\frac{\text{centimeter}}{\text{second}^2}`



Quantities of the same kind can be added:

>>> Quantity[6, "meter"] + Quantity[3, "centimeter"]
    =

:math:`603\text{ }\text{centimeter}`



Quantities of different kind can not:

>>> Quantity[6, "meter"] + Quantity[3, "second"]

    Quantity::compat second and meter are incompatible units.
    =

:math:`3\text{ }\text{second}+6\text{ }\text{meter}`


