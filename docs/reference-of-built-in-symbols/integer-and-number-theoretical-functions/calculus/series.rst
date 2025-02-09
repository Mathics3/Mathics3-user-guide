Series
======

`WMA link <https://reference.wolfram.com/language/ref/Series.html>`_


:code:`Series` [:math:`f`, {:math:`x`, :math:`x_0`, :math:`n`}]
    Represents the series expansion around :code:`:math:`x`=:math:`x_0``  up to order :math:`n`.





For elementary expressions, :code:`Series`  returns the explicit power series as a :code:`SeriesData`  expression:

>>> series = Series[Exp[x^2], {x,0,2}]

    =
:math:`1+x^2+O\left[x\right]^3`



The expression created is a :code:`SeriesData`  object:

>>> series // FullForm

    =
:math:`\text{SeriesData}\left[x, 0, \left\{1,0,1\right\}, 0, 3, 1\right]`



Replacing :math:`x` with does a value produces another :code:`SeriesData`  object:

>>> series /. x->4

    =
:math:`1+4^2+O\left[4\right]^3`



:code:`Normal`  transforms a :code:`SeriesData`  expression into a polynomial:

>>> series // Normal

    =
:math:`1+x^2`


>>> (series // Normal) /. x-> 4

    =
:math:`17`


>>> Clear[series];



We can also expand over multiple variables:

>>> Series[Exp[x-y], {x, 0, 2}, {y, 0, 2}]

    =
:math:`\left(1-y+\frac{1}{2} y^2+O\left[y\right]^3\right)+\left(1-y+\frac{1}{2} y^2+O\left[y\right]^3\right) x+\left(\frac{1}{2}+\left(-\frac{1}{2}\right) y+\frac{1}{4} y^2+O\left[y\right]^3\right) x^2+O\left[x\right]^3`



See also `:code:`SeriesCoefficient`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/seriescoefficient/>`_ and `:code:`SeriesData`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/calculus/seriesdata/>`_.