SeriesCoefficient
=================

`WMA link <https://reference.wolfram.com/language/ref/SeriesCoefficient.html>`_


:code:`SeriesCoefficient` [:math:`series`, :math:`n`]
    Find the :math:`n`th coefficient in the given :math:`series`.

:code:`SeriesCoefficient` [:math:`f`, {:math:`x`, :math:`x_0`, :math:`n`}]
    Find the (:math:`x`-:math:`x_0`)^n in the expansion of :math:`f` about the point :math:`x`=:math:`x_0`.





First we list 5 terms of a series:

>>> Series[Exp[Sin[x]], {x, 0, 5}]
  = 1 + x + 1 / 2 x ^ 2 + (-1 / 8) x ^ 4 + (-1 / 15) x ^ 5 + O[x] ^ 6

Now get the :math:`x`^4 coefficient:

>>> SeriesCoefficient[%, 4]
  = -1 / 8

Do the same thing, but without calling :code:`Series`  first:

>>> SeriesCoefficient[Exp[Sin[x]], {x, 0, 4}]
  = -1 / 8
>>> SeriesCoefficient[2x, {x, 0, 2}]
  = 0
>>> SeriesCoefficient[SeriesData[x, c, Table[i^2, {i, 10}], 7, 17, 3], 14/3]
  = 64
>>> SeriesCoefficient[SeriesData[x, c, Table[i^2, {i, 10}], 7, 17, 3], 6/3]
  = 0
>>> SeriesCoefficient[SeriesData[x, c, Table[i^2, {i, 10}], 7, 17, 3], 17/3]
  = Indeterminate

See also `:code:`Series`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/series/>`_ and `:code:`SeriesData`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/seriesdata/>`_.