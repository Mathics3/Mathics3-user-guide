FreeQ
=====

`WMA link <https://reference.wolfram.com/language/ref/FreeQ.html>`_


:code:`FreeQ` [:math:`expr`, :math:`x`]
    returns :code:`True`  if :math:`expr` does not contain the expression :math:`x`.





>>> FreeQ[y, x]
  = True
>>> FreeQ[a+b+c, a+b]
  = False
>>> FreeQ[{1, 2, a^(a+b)}, Plus]
  = False
>>> FreeQ[a+b, x_+y_+z_]
  = True
>>> FreeQ[a+b+c, x_+y_+z_]
  = False
>>> FreeQ[x_+y_+z_][a+b]
  = True
