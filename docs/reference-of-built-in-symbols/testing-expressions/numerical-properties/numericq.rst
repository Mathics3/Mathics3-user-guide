NumericQ
========

`WMA link <https://reference.wolfram.com/language/ref/NumericQ.html>`_


:code:`NumericQ` [:math:`expr`]
    tests whether :math:`expr` represents a numeric quantity.





>>> NumericQ[2]
  = True
>>> NumericQ[Sqrt[Pi]]
  = True
>>> NumberQ[Sqrt[Pi]]
  = False

It is possible to set that a symbol is numeric or not by assign a boolean value
to ``NumericQ``

>>> NumericQ[a]=True
  = True
>>> NumericQ[a]
  = True
>>> NumericQ[Sin[a]]
  = True

Clear and ClearAll do not restore the default value.

>>> Clear[a]; NumericQ[a]
  = True
>>> ClearAll[a]; NumericQ[a]
  = True
>>> NumericQ[a]=False; NumericQ[a]
  = False

NumericQ can only set to True or False

>>> NumericQ[a] = 37
  = 37
