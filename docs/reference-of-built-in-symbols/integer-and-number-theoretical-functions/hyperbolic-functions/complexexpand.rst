ComplexExpand
=============

(`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.expr.Expr.expand>`_, `WMA <https://reference.wolfram.com/language/ref/ComplexExpand.html>`_)


:code:`ComplexExpand` [:math:`expr`]
    expands :math:`expr` assuming that all variables are real.

:code:`ComplexExpand` [:math:`expr`,{:math:`x_1`,:math:`x_2`, ...}]
    expands :math:`expr` assuming that variables matching any of the :math:`xi` are complex.





Note: we get equivalent, but different results from WMA:

>>> ComplexExpand[3^(I x)]
  = 3 ^ (-Im[x]) Re[3 ^ (I Re[x])] + I Im[3 ^ (I Re[x])] 3 ^ (-Im[x])

Assume that both :math:`x` and :math:`y` and are real:

>>> ComplexExpand[Sin[x + I y]]
  = Cosh[y] Sin[x] + I Cos[x] Sinh[y]

Take :math:`x` to be complex:

>>> ComplexExpand[Sin[x], x]
  = Cosh[Im[x]] Sin[Re[x]] + I Cos[Re[x]] Sinh[Im[x]]

Polynomials:

>>> ComplexExpand[Re[z^5 - 2 z^3 - z + 1], z]
  = 1 + Re[z] ^ 5 - 2 Re[z] ^ 3 - Re[z] - 10 Im[z] ^ 2 Re[z] ^ 3 + 5 Im[z] ^ 4 Re[z] + 6 Im[z] ^ 2 Re[z]

Trigonometric and hyperbolic functions

>>> ComplexExpand[Cos[x + I y] + Tanh[z], {z}]
  = Cos[x] Cosh[y] - I Sin[x] Sinh[y] + Cosh[Re[z]] Sinh[Re[z]] / (Cos[Im[z]] ^ 2 + Sinh[Re[z]] ^ 2) + I Cos[Im[z]] Sin[Im[z]] / (Cos[Im[z]] ^ 2 + Sinh[Re[z]] ^ 2)

Exponential and logarithmic functions:

>>> ComplexExpand[Abs[2^z Log[2 z]], z]
  = Abs[I Arg[Re[z] + I Im[z]] + Log[4 Im[z] ^ 2 + 4 Re[z] ^ 2] / 2] 2 ^ Re[z]

Specify that variable :math:`z` is taken to be complex:

>>> ComplexExpand[Re[2 z^3 - z + 1], z]
  = 1 - Re[z] + 2 Re[z] ^ 3 - 6 Im[z] ^ 2 Re[z]
