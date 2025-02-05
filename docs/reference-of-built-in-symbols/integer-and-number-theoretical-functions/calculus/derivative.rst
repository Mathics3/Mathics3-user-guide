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
  = Cos[#1]&
>>> Derivative[3][Sin]
  = -Cos[#1]&
>>> Derivative[2][# ^ 3&]
  = 6 #1&

:code:`Derivative`  can be entered using :code:`\'` :

>>> Sin'[x]
  = Cos[x]
>>> (# ^ 4&)''
  = 12 #1 ^ 2&
>>> f'[x] // InputForm
  = Derivative[1][f][x]
>>> Derivative[1][#2 Sin[#1]+Cos[#2]&]
  = Cos[#1] #2&
>>> Derivative[1,2][#2^3 Sin[#1]+Cos[#2]&]
  = 6 Cos[#1] #2&

Deriving with respect to an unknown parameter yields 0:

>>> Derivative[1,2,1][#2^3 Sin[#1]+Cos[#2]&]
  = 0&

The 0th derivative of any expression is the expression itself:

>>> Derivative[0,0,0][a+b+c]
  = a + b + c

You can calculate the derivative of custom functions:

>>> f[x_] := x ^ 2

>>> f'[x]
  = 2 x

Unknown derivatives:

>>> Derivative[2, 1][h]
  = Derivative[2, 1][h]
>>> Derivative[2, 0, 1, 0][h[g]]
  = Derivative[2, 0, 1, 0][h[g]]
