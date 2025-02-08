Integrate
=========

`Integral <https://en.wikipedia.org/wiki/Integral>`_ (`SymPy <https://docs.sympy.org/latest/modules/integrals/integrals.html>`_, `WMA <https://reference.wolfram.com/language/ref/Integrate.html>`_)


:code:`Integrate` [:math:`f`, :math:`x`]
    integrates :math:`f` with respect to :math:`x`. The result does not contain the additive integration constant.

:code:`Integrate` [:math:`f`, {:math:`x`, :math:`a`, :math:`b`}]
    computes the definite integral of :math:`f` with respect to :math:`x` from :math:`a` to :math:`b`.





Integrate a polynomial:

>>> Integrate[6 x ^ 2 + 3 x ^ 2 - 4 x + 10, x]
    =

:math:`x \left(10-2 x+3 x^2\right)`



Integrate trigonometric functions:

>>> Integrate[Sin[x] ^ 5, x]
    =

:math:`\text{Cos}\left[x\right] \left(-1-\frac{\text{Cos}\left[x\right]^4}{5}+\frac{2 \text{Cos}\left[x\right]^2}{3}\right)`



Definite integrals:

>>> Integrate[x ^ 2 + x, {x, 1, 3}]
    =

:math:`\frac{38}{3}`


>>> Integrate[Sin[x], {x, 0, Pi/2}]
    =

:math:`1`



Some other integrals:

>>> Integrate[1 / (1 - 4 x + x^2), x]
    =

:math:`\frac{\sqrt{3} \left(\text{Log}\left[-2-\sqrt{3}+x\right]-\text{Log}\left[-2+\sqrt{3}+x\right]\right)}{6}`


>>> Integrate[4 Sin[x] Cos[x], x]
    =

:math:`2 \text{Sin}\left[x\right]^2`


>>> Integrate[-Infinity, {x, 0, Infinity}]
    =

:math:`-\infty`



Integrating something ill-defined returns the expression untouched:

>>> Integrate[1, {x, Infinity, 0}]
    =

:math:`\int_{\infty }^0 1 \, dx`



Here how is an example of converting integral equation to TeX:

>>> Integrate[f[x], {x, a, b}] // TeXForm
    =

:math:`\text{$\backslash$int\_a${}^{\wedge}$b f$\backslash$left[x$\backslash$right] $\backslash$, dx}`



Sometimes there is a loss of precision during integration.
You can check the precision of your result with the following sequence of commands.

>>> Integrate[Abs[Sin[phi]], {phi, 0, 2Pi}] // N
    =

:math:`4.`


>>> % // Precision
    =

:math:`\text{MachinePrecision}`


>>> Integrate[ArcSin[x / 3], x]
    =

:math:`x \text{ArcSin}\left[\frac{x}{3}\right]+\sqrt{9-x^2}`


>>> Integrate[f'[x], {x, a, b}]
    =

:math:`f\left[b\right]-f\left[a\right]`



and,

>>> D[Integrate[f[u, x],{u, a[x], b[x]}], x]
    =

:math:`\int_{a\left[x\right]}^{b\left[x\right]} f^{\left(0,1\right)}\left[u,x\right] \, du+f\left[b\left[x\right],x\right] b'\left[x\right]-f\left[a\left[x\right],x\right] a'\left[x\right]`


>>> N[Integrate[Sin[Exp[-x^2 /2 ]],{x,1,2}]]
    =

:math:`0.330804`


