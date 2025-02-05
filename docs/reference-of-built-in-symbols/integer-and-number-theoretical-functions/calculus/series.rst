Series
======

`WMA link <https://reference.wolfram.com/language/ref/Series.html>`_


:code:`Series` [:math:`f`, {:math:`x`, :math:`x_0`, :math:`n`}]
    Represents the series expansion around :code:`:math:`x`=:math:`x_0``  up to order :math:`n`.





For elementary expressions, :code:`Series`  returns the explicit power series as a :code:`SeriesData`  expression:

>>> series = Series[Exp[x^2], {x,0,2}]
  = 1 + x ^ 2 + O[x] ^ 3

The expression created is a :code:`SeriesData`  object:

>>> series // FullForm
  = SeriesData[x, 0, {1,0,1}, 0, 3, 1]

Replacing :math:`x` with does a value produces another :code:`SeriesData`  object:

>>> series /. x->4
  = 1 + 4 ^ 2 + O[4] ^ 3

:code:`Normal`  transforms a :code:`SeriesData`  expression into a polynomial:

>>> series // Normal
  = 1 + x ^ 2
>>> (series // Normal) /. x-> 4
  = 17
>>> Clear[series];


We can also expand over multiple variables:

>>> Series[Exp[x-y], {x, 0, 2}, {y, 0, 2}]
  = (1 - y + 1 / 2 y ^ 2 + O[y] ^ 3) + (1 - y + 1 / 2 y ^ 2 + O[y] ^ 3) x + (1 / 2 + (-1 / 2) y + 1 / 4 y ^ 2 + O[y] ^ 3) x ^ 2 + O[x] ^ 3

See also `:code:`SeriesCoefficient`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/seriescoefficient/>`_ and `:code:`SeriesData`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/seriesdata/>`_.