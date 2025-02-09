Apart
=====

`WMA link <https://reference.wolfram.com/language/ref/Apart.html>`_


:code:`Apart` [:math:`expr`]
    writes :math:`expr` as a sum of individual fractions.

:code:`Apart` [:math:`expr`, :math:`var`]
    treats :math:`var` as the main variable.





>>> Apart[1 / (x^2 + 5x + 6)]

    =
:math:`\frac{1}{2+x}-\frac{1}{3+x}`



When several variables are involved, the results can be different
depending on the main variable:

>>> Apart[1 / (x^2 - y^2), x]

    =
:math:`-\frac{1}{2 y \left(x+y\right)}+\frac{1}{2 y \left(x-y\right)}`


>>> Apart[1 / (x^2 - y^2), y]

    =
:math:`\frac{1}{2 x \left(x+y\right)}+\frac{1}{2 x \left(x-y\right)}`



:code:`Apart`  is :code:`Listable` :

>>> Apart[{1 / (x^2 + 5x + 6)}]

    =
:math:`\left\{\frac{1}{2+x}-\frac{1}{3+x}\right\}`



But it does not touch other expressions:

>>> Sin[1 / (x ^ 2 - y ^ 2)] // Apart

    =
:math:`\text{Sin}\left[\frac{1}{x^2-y^2}\right]`


