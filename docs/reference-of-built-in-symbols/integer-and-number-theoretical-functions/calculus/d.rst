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

    =
:math:`2 x+3 x^2`



Second-order derivative:

>>> D[x^3 + x^2, {x, 2}]

    =
:math:`2+6 x`



Trigonometric derivatives:

>>> D[Sin[Cos[x]], x]

    =
:math:`-\text{Cos}\left[\text{Cos}\left[x\right]\right] \text{Sin}\left[x\right]`


>>> D[Sin[x], {x, 2}]

    =
:math:`-\text{Sin}\left[x\right]`


>>> D[Cos[t], {t, 2}]

    =
:math:`-\text{Cos}\left[t\right]`



Unknown variables are treated as constant:

>>> D[y, x]

    =
:math:`0`


>>> D[x, x]

    =
:math:`1`


>>> D[x + y, x]

    =
:math:`1`



Derivatives of unknown functions are represented using :code:`Derivative` :

>>> D[f[x], x]

    =
:math:`f'\left[x\right]`


>>> D[f[x, x], x]

    =
:math:`f^{\left(0,1\right)}\left[x,x\right]+f^{\left(1,0\right)}\left[x,x\right]`


>>> D[f[x, x], x] // InputForm

    =
:math:`\text{Derivative}\left[0, 1\right]\left[f\right]\left[x, x\right]\text{ + }\text{Derivative}\left[1, 0\right]\left[f\right]\left[x, x\right]`



Chain rule:

>>> D[f[2x+1, 2y, x+y], x]

    =
:math:`2 f^{\left(1,0,0\right)}\left[1+2 x,2 y,x+y\right]+f^{\left(0,0,1\right)}\left[1+2 x,2 y,x+y\right]`


>>> D[f[x^2, x, 2y], {x,2}, y] // Expand

    =
:math:`8 x f^{\left(1,1,1\right)}\left[x^2,x,2 y\right]+8 x^2 f^{\left(2,0,1\right)}\left[x^2,x,2 y\right]+2 f^{\left(0,2,1\right)}\left[x^2,x,2 y\right]+4 f^{\left(1,0,1\right)}\left[x^2,x,2 y\right]`



Compute the gradient vector of a function:

>>> D[x ^ 3 * Cos[y], {{x, y}}]

    =
:math:`\left\{3 x^2 \text{Cos}\left[y\right],-x^3 \text{Sin}\left[y\right]\right\}`



Hesse matrix:

>>> D[Sin[x] * Cos[y], {{x,y}, 2}]

    =
:math:`\left\{\left\{-\text{Cos}\left[y\right] \text{Sin}\left[x\right],-\text{Cos}\left[x\right] \text{Sin}\left[y\right]\right\},\left\{-\text{Cos}\left[x\right] \text{Sin}\left[y\right],-\text{Cos}\left[y\right] \text{Sin}\left[x\right]\right\}\right\}`


