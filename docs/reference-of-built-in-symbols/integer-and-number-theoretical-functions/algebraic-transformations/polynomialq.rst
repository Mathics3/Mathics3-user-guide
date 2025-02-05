PolynomialQ
===========

`Polynomial <https://en.wikipedia.org/wiki/Polynomial:>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.expr.Expr.is_polynomial>`_, `WMA <https://reference.wolfram.com/language/ref/PolynomialQ.html>`_)


:code:`PolynomialQ[expr]`
    returns True if :math:`expr` is a polynomial and returns False otherwise.

:code:`PolynomialQ[expr, var]`
    returns True if :math:`expr` is a polynomial in :math:`var`, and returns False otherwise.

:code:`PolynomialQ[expr, {var1, ...}]`
    tests whether :math:`expr` is a polynomial in the :math:`vari`.






:code:`PolynomialQ`  with no explicit variable mentioned:

>>> PolynomialQ[x^2]
  = True

A number is a degenerate kind of polynomial:

>>> PolynomialQ[2]
  = True

The following is not a polynomial because :math:`y` is raised to     the power -1:

>>> PolynomialQ[x^2 + x/y]
  = False

:code:`PolynomialQ`  using an expression and a single variable:

>>> PolynomialQ[x^3 - 2 x/y + 3xz, x]
  = True

In the above, there were no negative powers for :math:`x`.     In the below when we check with respect to :math:`y`,     we *do* find :math:`y` is raised to a negative power:

>>> PolynomialQ[x^3 - 2 x/y^2 + 3xz, y]
  = False
>>> PolynomialQ[f[a] + f[a]^2, f[a]]
  = True

:code:`PolynomialQ`  using an expression and a list of variables:

>>> PolynomialQ[x^2 + axy^2 - bSin[c], {x, y}]
  = True
>>> PolynomialQ[x^2 + axy^2 - bSin[c], {a, b, c}]
  = False
