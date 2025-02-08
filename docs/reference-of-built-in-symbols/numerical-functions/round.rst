Round
=====

`WMA link <https://reference.wolfram.com/language/ref/Round.html>`_


:code:`Round` [:math:`expr`]
    rounds :math:`expr` to the nearest integer.

:code:`Round` [:math:`expr`, :math:`k`]
    rounds :math:`expr` to the closest multiple of :math:`k`.





>>> Round[10.6]
    =

:math:`11`


>>> Round[0.06, 0.1]
    =

:math:`0.1`


>>> Round[0.04, 0.1]
    =

:math:`0.`



Constants can be rounded too

>>> Round[Pi, .5]
    =

:math:`3.`


>>> Round[Pi^2]
    =

:math:`10`



Round to exact value

>>> Round[2.6, 1/3]
    =

:math:`\frac{8}{3}`


>>> Round[10, Pi]
    =

:math:`3  \pi`



Round complex numbers

>>> Round[6/(2 + 3 I)]
    =

:math:`1-I`


>>> Round[1 + 2 I, 2 I]
    =

:math:`2 I`



Round Negative numbers too

>>> Round[-1.4]
    =

:math:`-1`



Expressions other than numbers remain unevaluated:

>>> Round[x]
    =

:math:`\text{Round}\left[x\right]`


>>> Round[1.5, k]
    =

:math:`\text{Round}\left[1.5,k\right]`


