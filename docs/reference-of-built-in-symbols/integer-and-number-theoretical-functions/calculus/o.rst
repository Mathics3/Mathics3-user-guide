O
=

`WMA link <https://reference.wolfram.com/language/ref/O.html>`_


:code:`O[:math:`x`]^n`
    Represents a term of order :math:`x^n`.

    O[x]^n is generated to represent omitted higher order terms in            power series.





>>> Series[1/(1-x),{x,0,2}]

    =
:math:`1+x+x^2+O\left[x\right]^3`



When called alone, a `SeriesData` expression is built:

>>> O[x] // FullForm

    =
:math:`\text{SeriesData}\left[x, 0, \left\{\right\}, 1, 1, 1\right]`


