ExpandDenominator
=================

`WMA link <https://reference.wolfram.com/language/ref/ExpandDenominator.html>`_


:code:`ExpandDenominator` [:math:`expr`]
    expands out negative integer powers and products of sums in :math:`expr`.





>>> ExpandDenominator[(a + b) ^ 2 / ((c + d)^2 (e + f))]

    =
:math:`\frac{\left(a+b\right)^2}{c^2 e+c^2 f+2 c d e+2 c d f+d^2 e+d^2 f}`


