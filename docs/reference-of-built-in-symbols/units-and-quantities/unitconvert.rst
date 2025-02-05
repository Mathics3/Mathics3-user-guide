UnitConvert
===========

`WMA link <https://reference.wolfram.com/language/ref/UnitConvert.html>`_


:code:`UnitConvert[:math:`quantity`, :math:`targetunit`] `
    converts the specified :math:`quantity` to the specified :math:`targetunit`.

:code:`UnitConvert[quantity]`
    converts the specified :math:`quantity` to its "SIBase" units.





Convert from miles to kilometers:

>>> UnitConvert[Quantity[5.2, "miles"], "kilometers"]
  = 8.36859 kilometer

Convert a Quantity object to the appropriate SI base units:

>>> UnitConvert[Quantity[3.8, "Pounds"]]
  = 1.72365 kilogram
