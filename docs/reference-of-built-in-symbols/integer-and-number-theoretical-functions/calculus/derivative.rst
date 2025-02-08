Derivative
==========

`WMA link <https://reference.wolfram.com/language/ref/Derivative.html>`_


:math:`f`:code:`'` [:math:`x`,...]
    represents the derivative of :math:`f` with respect to the first argument :math:`x`.

:math:`f`:code:`''` [:math:`x`,...]
    represents the 2nd derivative of :math:`f` with respect to :math:`x`.

:code:`Derivative` [:math:`n`][:math:`f`]
    represents the :math:`n`th derivative of the function :math:`f`.

:code:`Derivative` [:math:`n_1`, :math:`n_2`, ...][:math:`f`]
    represents a multivariate derivative.





>>> Derivative[1][Sin]
    =

:math:`\text{Cos}\left[\text{\#1}\right]\&`


>>> Derivative[3][Sin]
    =

:math:`-\text{Cos}\left[\text{\#1}\right]\&`


>>> Derivative[2][# ^ 3&]
    =

:math:`6 \text{\#1}\&`



:code:`Derivative`  can be entered using :code:`\'` :

>>> Sin'[x]
    =

:math:`\text{Cos}\left[x\right]`


>>> (# ^ 4&)''
    =

:math:`12 \text{\#1}^2\&`


>>> f'[x] // InputForm
    =

:math:`\text{Derivative}\left[1\right]\left[f\right]\left[x\right]`


>>> Derivative[1][#2 Sin[#1]+Cos[#2]&]
    =

:math:`\text{Cos}\left[\text{\#1}\right] \text{\#2}\&`


>>> Derivative[1,2][#2^3 Sin[#1]+Cos[#2]&]
    =

:math:`6 \text{Cos}\left[\text{\#1}\right] \text{\#2}\&`



Deriving with respect to an unknown parameter yields 0:

>>> Derivative[1,2,1][#2^3 Sin[#1]+Cos[#2]&]
    =

:math:`0\&`



The 0th derivative of any expression is the expression itself:

>>> Derivative[0,0,0][a+b+c]
    =

:math:`a+b+c`



You can calculate the derivative of custom functions:

>>> f[x_] := x ^ 2


>>> f'[x]
    =

:math:`2 x`



Unknown derivatives:

>>> Derivative[2, 1][h]
    =

:math:`h^{\left(2,1\right)}`


>>> Derivative[2, 0, 1, 0][h[g]]
    =

:math:`h\left[g\right]^{\left(2,0,1,0\right)}`


