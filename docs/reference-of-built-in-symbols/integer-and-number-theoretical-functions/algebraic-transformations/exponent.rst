Exponent
========

`WMA link <https://reference.wolfram.com/language/ref/Exponent.html>`_


:code:`Exponent[expr, form]`
    returns the maximum power with which :math:`form` appears in the expanded           form of :math:`expr`.

:code:`Exponent[expr, form, h]`
    applies :math:`h` to the set of exponents with which :math:`form` appears in :math:`expr`.





>>> Exponent[5 x^2 - 3 x + 7, x]
    =

:math:`2`


>>> Exponent[(x^3 + 1)^2 + 1, x]
    =

:math:`6`


>>> Exponent[x^(n + 1) + Sqrt[x] + 1, x]
    =

:math:`\text{Max}\left[\frac{1}{2},1+n\right]`


>>> Exponent[x / y, y]
    =

:math:`-1`


>>> Exponent[(x^2 + 1)^3 - 1, x, Min]
    =

:math:`2`


>>> Exponent[0, x]
    =

:math:`-\infty`


>>> Exponent[1, x]
    =

:math:`0`


