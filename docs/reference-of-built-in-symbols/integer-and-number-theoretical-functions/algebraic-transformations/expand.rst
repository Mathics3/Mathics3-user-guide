Expand
======

`WMA link <https://reference.wolfram.com/language/ref/Expand.html>`_


:code:`Expand` [:math:`expr`]
    expands out positive integer powers and products of sums in :math:`expr`, as           well as trigonometric identities.

Expand[:math:`expr`, :math:`target`]
    just expands those parts involving :math:`target`.





>>> Expand[(x + y) ^ 3]
    =

:math:`x^3+3 x^2 y+3 x y^2+y^3`


>>> Expand[(a + b) (a + c + d)]
    =

:math:`a^2+a b+a c+a d+b c+b d`


>>> Expand[(a + b) (a + c + d) (e + f) + e a a]
    =

:math:`2 a^2 e+a^2 f+a b e+a b f+a c e+a c f+a d e+a d f+b c e+b c f+b d e+b d f`


>>> Expand[(a + b) ^ 2 * (c + d)]
    =

:math:`a^2 c+a^2 d+2 a b c+2 a b d+b^2 c+b^2 d`


>>> Expand[(x + y) ^ 2 + x y]
    =

:math:`x^2+3 x y+y^2`


>>> Expand[((a + b) (c + d)) ^ 2 + b (1 + a)]
    =

:math:`a^2 c^2+2 a^2 c d+a^2 d^2+b+a b+2 a b c^2+4 a b c d+2 a b d^2+b^2 c^2+2 b^2 c d+b^2 d^2`



:code:`Expand`  expands items in lists and rules:

>>> Expand[{4 (x + y), 2 (x + y) -> 4 (x + y)}]
    =

:math:`\left\{4 x+4 y,2 x+2 y->4 x+4 y\right\}`



:code:`Expand`  expands trigonometric identities

>>> Expand[Sin[x + y], Trig -> True]
    =

:math:`\text{Cos}\left[x\right] \text{Sin}\left[y\right]+\text{Cos}\left[y\right] \text{Sin}\left[x\right]`


>>> Expand[Tanh[x + y], Trig -> True]
    =

:math:`\frac{\text{Cosh}\left[x\right] \text{Sinh}\left[y\right]}{\text{Cosh}\left[x\right] \text{Cosh}\left[y\right]+\text{Sinh}\left[x\right] \text{Sinh}\left[y\right]}+\frac{\text{Cosh}\left[y\right] \text{Sinh}\left[x\right]}{\text{Cosh}\left[x\right] \text{Cosh}\left[y\right]+\text{Sinh}\left[x\right] \text{Sinh}\left[y\right]}`



:code:`Expand`  does not change any other expression.

>>> Expand[Sin[x (1 + y)]]
    =

:math:`\text{Sin}\left[x \left(1+y\right)\right]`



Using the second argument, the expression only
expands those subexpressions containing :math:`pat`:

>>> Expand[(x+a)^2+(y+a)^2+(x+y)(x+a), y]
    =

:math:`a^2+2 a y+x \left(a+x\right)+y \left(a+x\right)+y^2+\left(a+x\right)^2`



:code:`Expand`  also works in Galois fields

>>> Expand[(1 + a)^12, Modulus -> 3]
    =

:math:`1+a^3+a^9+a^{12}`


>>> Expand[(1 + a)^12, Modulus -> 4]
    =

:math:`1+2 a^2+3 a^4+3 a^8+2 a^{10}+a^{12}`


