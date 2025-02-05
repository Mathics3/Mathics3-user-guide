Coefficient
===========

`WMA link <https://reference.wolfram.com/language/ref/Coefficient.html>`_


:code:`Coefficient[expr, form]`
    returns the coefficient of :math:`form` in the polynomial :math:`expr`.

:code:`Coefficient[expr, form, n]`
    return the coefficient of :math:`form`^:math:`n` in :math:`expr`.





>>> Coefficient[(x + y)^4, (x^2) * (y^2)]
  = 6
>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, x]
  = c
>>> Coefficient[(x + 3 y)^5, x]
  = 405 y ^ 4
>>> Coefficient[(x + 3 y)^5, x * y^4]
  = 405
>>> Coefficient[(x + 2)/(y - 3) + (x + 3)/(y - 2), x]
  = 1 / (-3 + y) + 1 / (-2 + y)
>>> Coefficient[x*Cos[x + 3] + 6*y, x]
  = Cos[3 + x]
>>> Coefficient[(x + 1)^3, x, 2]
  = 3
>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, y, 3]
  = b

Find the free term in a polynomial:

>>> Coefficient[(x + 2)^3 + (x + 3)^2, x, 0]
  = 17
>>> Coefficient[(x + 2)^3 + (x + 3)^2, y, 0]
  = (2 + x) ^ 3 + (3 + x) ^ 2
>>> Coefficient[a x^2 + b y^3 + c x + d y + 5, x, 0]
  = 5 + b y ^ 3 + d y
