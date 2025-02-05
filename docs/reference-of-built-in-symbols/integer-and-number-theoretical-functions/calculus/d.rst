D
=

`Derivative <https://en.wikipedia.org/wiki/Derivative>`_    (`WMA <https://reference.wolfram.com/language/ref/D.html>`_)


:code:`D` [:math:`f`, :math:`x`]
    gives the partial derivative of :math:`f` with respect to :math:`x`.

:code:`D` [:math:`f`, :math:`x`, :math:`y`, ...]
    differentiates successively with respect to :math:`x`, :math:`y`, etc.

:code:`D` [:math:`f`, {:math:`x`, :math:`n`}]
    gives the multiple derivative of order :math:`n`.

:code:`D` [:math:`f`, {{:math:`x_1`, :math:`x_2`, ...}}]
    gives the vector derivative of :math:`f` with respect to :math:`x_1`, :math:`x_2`, etc.





First-order derivative of a polynomial:

>>> D[x^3 + x^2, x]
  = 2 x + 3 x ^ 2

Second-order derivative:

>>> D[x^3 + x^2, {x, 2}]
  = 2 + 6 x

Trigonometric derivatives:

>>> D[Sin[Cos[x]], x]
  = -Cos[Cos[x]] Sin[x]
>>> D[Sin[x], {x, 2}]
  = -Sin[x]
>>> D[Cos[t], {t, 2}]
  = -Cos[t]

Unknown variables are treated as constant:

>>> D[y, x]
  = 0
>>> D[x, x]
  = 1
>>> D[x + y, x]
  = 1

Derivatives of unknown functions are represented using :code:`Derivative` :

>>> D[f[x], x]
  = f'[x]
>>> D[f[x, x], x]
  = Derivative[0, 1][f][x, x] + Derivative[1, 0][f][x, x]
>>> D[f[x, x], x] // InputForm
  = Derivative[0, 1][f][x, x] + Derivative[1, 0][f][x, x]

Chain rule:

>>> D[f[2x+1, 2y, x+y], x]
  = 2 Derivative[1, 0, 0][f][1 + 2 x, 2 y, x + y] + Derivative[0, 0, 1][f][1 + 2 x, 2 y, x + y]
>>> D[f[x^2, x, 2y], {x,2}, y] // Expand
  = 8 x Derivative[1, 1, 1][f][x ^ 2, x, 2 y] + 8 x ^ 2 Derivative[2, 0, 1][f][x ^ 2, x, 2 y] + 2 Derivative[0, 2, 1][f][x ^ 2, x, 2 y] + 4 Derivative[1, 0, 1][f][x ^ 2, x, 2 y]

Compute the gradient vector of a function:

>>> D[x ^ 3 * Cos[y], {{x, y}}]
  = {3 x ^ 2 Cos[y], -x ^ 3 Sin[y]}

Hesse matrix:

>>> D[Sin[x] * Cos[y], {{x,y}, 2}]
  = {{-Cos[y] Sin[x], -Cos[x] Sin[y]}, {-Cos[x] Sin[y], -Cos[y] Sin[x]}}
