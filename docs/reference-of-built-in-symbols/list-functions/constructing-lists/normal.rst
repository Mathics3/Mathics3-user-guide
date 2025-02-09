Normal
======

`WMA link <https://reference.wolfram.com/language/ref/Normal.html>`_


:code:`Normal[expr_]`
    Brings special expressions to a normal expression from different special            forms.





>>> Normal[Pi]

    =
:math:`\pi`


>>> Series[Exp[x], {x, 0, 5}]

    =
:math:`1+x+\frac{1}{2} x^2+\frac{1}{6} x^3+\frac{1}{24} x^4+\frac{1}{120} x^5+O\left[x\right]^6`


>>> Normal[%]

    =
:math:`1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\frac{x^5}{120}`


