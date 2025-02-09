Cancel
======

`WMA link <https://reference.wolfram.com/language/ref/Cancel.html>`_


:code:`Cancel` [:math:`expr`]
    cancels out common factors in numerators and denominators.





>>> Cancel[x / x ^ 2]

    =
:math:`\frac{1}{x}`



:code:`Cancel`  threads over sums:

>>> Cancel[x / x ^ 2 + y / y ^ 2]

    =
:math:`\frac{1}{x}+\frac{1}{y}`


>>> Cancel[f[x] / x + x * f[x] / x ^ 2]

    =
:math:`\frac{2 f\left[x\right]}{x}`


