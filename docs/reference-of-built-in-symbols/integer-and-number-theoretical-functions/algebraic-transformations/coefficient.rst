Coefficient
===========

`WMA link <https://reference.wolfram.com/language/ref/Coefficient.html>`_


:code:`Coefficient[expr, form]`
    returns the coefficient of :math:`form` in the polynomial :math:`expr`.

:code:`Coefficient[expr, form, n]`
    return the coefficient of :math:`form`^:math:`n` in :math:`expr`.





>>> Coefficient[(x + y)^4, (x^2) * (y^2)]

    =
:math:`6`


>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, x]

    =
:math:`c`


>>> Coefficient[(x + 3 y)^5, x]

    =
:math:`405 y^4`


>>> Coefficient[(x + 3 y)^5, x * y^4]

    =
:math:`405`


>>> Coefficient[(x + 2)/(y - 3) + (x + 3)/(y - 2), x]

    =
:math:`\frac{1}{-3+y}+\frac{1}{-2+y}`


>>> Coefficient[x*Cos[x + 3] + 6*y, x]

    =
:math:`\text{Cos}\left[3+x\right]`


>>> Coefficient[(x + 1)^3, x, 2]

    =
:math:`3`


>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, y, 3]

    =
:math:`b`



Find the free term in a polynomial:

>>> Coefficient[(x + 2)^3 + (x + 3)^2, x, 0]

    =
:math:`17`


>>> Coefficient[(x + 2)^3 + (x + 3)^2, y, 0]

    =
:math:`\left(2+x\right)^3+\left(3+x\right)^2`


>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, x, 0]

    =
:math:`5+b y^3+d y`


