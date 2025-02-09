NumericQ
========

`WMA link <https://reference.wolfram.com/language/ref/NumericQ.html>`_


:code:`NumericQ` [:math:`expr`]
    tests whether :math:`expr` represents a numeric quantity.





>>> NumericQ[2]

    =
:math:`\text{True}`


>>> NumericQ[Sqrt[Pi]]

    =
:math:`\text{True}`


>>> NumberQ[Sqrt[Pi]]

    =
:math:`\text{False}`



It is possible to set that a symbol is numeric or not by assign a boolean value
to ``NumericQ``

>>> NumericQ[a]=True

    =
:math:`\text{True}`


>>> NumericQ[a]

    =
:math:`\text{True}`


>>> NumericQ[Sin[a]]

    =
:math:`\text{True}`



Clear and ClearAll do not restore the default value.

>>> Clear[a]; NumericQ[a]

    =
:math:`\text{True}`


>>> ClearAll[a]; NumericQ[a]

    =
:math:`\text{True}`


>>> NumericQ[a]=False; NumericQ[a]

    =
:math:`\text{False}`



NumericQ can only set to True or False

>>> NumericQ[a] = 37

    NumericQ::set Cannot set NumericQ[a] to 37; the lhs argument must be a symbol and the rhs must be True or False.

    =
:math:`37`


