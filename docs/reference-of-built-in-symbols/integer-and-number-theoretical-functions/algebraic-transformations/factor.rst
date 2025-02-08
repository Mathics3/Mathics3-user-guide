Factor
======

`WMA link <https://reference.wolfram.com/language/ref/Factor.html>`_


:code:`Factor` [:math:`expr`]
    factors the polynomial expression :math:`expr`.





>>> Factor[x ^ 2 + 2 x + 1]
    =

:math:`\left(1+x\right)^2`


>>> Factor[1 / (x^2+2x+1) + 1 / (x^4+2x^2+1)]
    =

:math:`\frac{2+2 x+3 x^2+x^4}{\left(1+x\right)^2 {\left(1+x^2\right)}^2}`



Factor can also be used with equations:

>>> Factor[x a == x b + x c]
    =

:math:`a x\text{==}x \left(b+c\right)`



And lists:

>>> Factor[{x + x^2, 2 x + 2 y + 2}]
    =

:math:`\left\{x \left(1+x\right),2 \left(1+x+y\right)\right\}`



It also works with more complex expressions:

>>> Factor[x ^ 3 + 3 x ^ 2 y + 3 x y ^ 2 + y ^ 3]
    =

:math:`\left(x+y\right)^3`



You can use Factor to find when a polynomial is zero:

>>> x^2 - x == 0 // Factor
    =

:math:`x \left(-1+x\right)\text{==}0`


