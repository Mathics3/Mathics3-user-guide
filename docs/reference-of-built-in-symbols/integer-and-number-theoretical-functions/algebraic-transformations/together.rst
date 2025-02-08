Together
========

`WMA link <https://reference.wolfram.com/language/ref/Together.html>`_


:code:`Together` [:math:`expr`]
    writes sums of fractions in :math:`expr` together.





>>> Together[a / c + b / c]
    =

:math:`\frac{a+b}{c}`



:code:`Together`  operates on lists:

>>> Together[{x / (y+1) + x / (y+1)^2}]
    =

:math:`\left\{\frac{x \left(2+y\right)}{\left(1+y\right)^2}\right\}`



But it does not touch other functions:

>>> Together[f[a / c + b / c]]
    =

:math:`f\left[\frac{a}{c}+\frac{b}{c}\right]`


