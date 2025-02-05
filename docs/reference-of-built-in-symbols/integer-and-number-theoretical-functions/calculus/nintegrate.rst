NIntegrate
==========

`WMA link <https://reference.wolfram.com/language/ref/NIntegrate.html>`_


:code:`NIntegrate` [:math:`expr`, :math:`interval`]
    returns a numeric approximation to the definite integral of :math:`expr` with            limits :math:`interval` and with a precision of :math:`prec` digits.

:code:`NIntegrate` [:math:`expr`, :math:`interval_1`, :math:`interval_2`, ...]
    returns a numeric approximation to the multiple integral of :math:`expr` with             limits :math:`interval_1`, :math:`interval_2` and with a precision of :math:`prec` digits.





>>> NIntegrate[Exp[-x],{x,0,Infinity},Tolerance->1*^-6, Method->"Internal"]
  = 1.
>>> NIntegrate[Exp[x],{x,-Infinity, 0},Tolerance->1*^-6, Method->"Internal"]
  = 1.
>>> NIntegrate[Exp[-x^2/2.],{x,-Infinity, Infinity},Tolerance->1*^-6, Method->"Internal"]
  = 2.5066...
