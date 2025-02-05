Integrate
=========

`Integral <https://en.wikipedia.org/wiki/Integral>`_ (`SymPy <https://docs.sympy.org/latest/modules/integrals/integrals.html>`_, `WMA <https://reference.wolfram.com/language/ref/Integrate.html>`_)


:code:`Integrate` [:math:`f`, :math:`x`]
    integrates :math:`f` with respect to :math:`x`. The result does not contain the additive integration constant.

:code:`Integrate` [:math:`f`, {:math:`x`, :math:`a`, :math:`b`}]
    computes the definite integral of :math:`f` with respect to :math:`x` from :math:`a` to :math:`b`.





Integrate a polynomial:

>>> Integrate[6 x ^ 2 + 3 x ^ 2 - 4 x + 10, x]
  = x (10 - 2 x + 3 x ^ 2)

Integrate trigonometric functions:

>>> Integrate[Sin[x] ^ 5, x]
  = Cos[x] (-1 - Cos[x] ^ 4 / 5 + 2 Cos[x] ^ 2 / 3)

Definite integrals:

>>> Integrate[x ^ 2 + x, {x, 1, 3}]
  = 38 / 3
>>> Integrate[Sin[x], {x, 0, Pi/2}]
  = 1

Some other integrals:

>>> Integrate[1 / (1 - 4 x + x^2), x]
  = Sqrt[3] (Log[-2 - Sqrt[3] + x] - Log[-2 + Sqrt[3] + x]) / 6
>>> Integrate[4 Sin[x] Cos[x], x]
  = 2 Sin[x] ^ 2
>>> Integrate[-Infinity, {x, 0, Infinity}]
  = -Infinity

Integrating something ill-defined returns the expression untouched:

>>> Integrate[1, {x, Infinity, 0}]
  = Integrate[1, {x, Infinity, 0}]

Here how is an example of converting integral equation to TeX:

>>> Integrate[f[x], {x, a, b}] // TeXForm
  = \int_a^b f\left[x\right] \, dx

Sometimes there is a loss of precision during integration.
You can check the precision of your result with the following sequence of commands.

>>> Integrate[Abs[Sin[phi]], {phi, 0, 2Pi}] // N
  = 4.
>>> % // Precision
  = MachinePrecision
>>> Integrate[ArcSin[x / 3], x]
  = x ArcSin[x / 3] + Sqrt[9 - x ^ 2]
>>> Integrate[f'[x], {x, a, b}]
  = f[b] - f[a]

and,

>>> D[Integrate[f[u, x],{u, a[x], b[x]}], x]
  = Integrate[Derivative[0, 1][f][u, x], {u, a[x], b[x]}] + f[b[x], x] b'[x] - f[a[x], x] a'[x]
>>> N[Integrate[Sin[Exp[-x^2 /2 ]],{x,1,2}]]
  = 0.330804
