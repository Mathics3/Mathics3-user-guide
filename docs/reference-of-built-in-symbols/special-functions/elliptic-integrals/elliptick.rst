EllipticK
=========

`Complete elliptic integral of the first kind <https://en.wikipedia.org/wiki/Elliptic_integral#Complete_elliptic_integral_of_the_first_kind>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html>`_, `WMA <https://reference.wolfram.com/language/ref/EllipticK.html>`_)


:code:`EllipticK` [:math:`m`]
    computes the elliptic integral of the first kind :math:`K(m)`.





>>> EllipticK[0.5]

    =
:math:`1.85407`



Elliptic curves give Pi / 2 when evaluated at zero:

>>> EllipticK[0]

    =
:math:`\frac{ \pi }{2}`



Plot over a reals around 0:

>>> Plot[EllipticK[n], {n, -1, 1}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_EllipticK_f_dr_sq3.png
    :align: center



