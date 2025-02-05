EllipticF
=========

`Complete elliptic integral of the first kind <https://en.wikipedia.org/wiki/ Elliptic_integral#Complete_elliptic_integral_of_the_first_kind>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/ special.html#sympy.functions.special.elliptic_integrals.elliptic_f>`_, `WMA <https://reference.wolfram.com/language/ref/EllipticF.html>`_)


:code:`EllipticF` [:math:`\phi`, :math:`m`]
    computes the elliptic integral of the first kind :math:`F(\phi|m)`.





>>> EllipticF[0.3, 0.8]
  = 0.303652

EllipticF is zero when the first argument is zero:

>>> EllipticF[0, 0.8]
  = 0
