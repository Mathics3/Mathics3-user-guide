EllipticE
=========

`Elliptic complete elliptic integral of the second kind <https://en.wikipedia.org/wiki/Elliptic_integral#Complete_elliptic_integral_of_the_second_kind>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.elliptic_integrals.elliptic_e>`_, `WMA <https://reference.wolfram.com/language/ref/EllipticE.html>`_)


:code:`EllipticE` [:math:`m`]
    computes the complete elliptic integral :math:`E(m)`.

:code:`EllipticE` [:math:`\phi`|:math:`m`]
    computes the complete elliptic integral of the second kind :math:`E(m|\phi)`.





Elliptic curves give Pi / 2 when evaluated at zero:

>>> EllipticE[0]

    =
:math:`\frac{ \pi }{2}`


>>> EllipticE[0.3, 0.8]

    =
:math:`0.296426`



Plot over a reals centered around 0:

>>> Plot[EllipticE[m], {m, -2, 2}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_EllipticE_g72w1se5.png
    :align: center



