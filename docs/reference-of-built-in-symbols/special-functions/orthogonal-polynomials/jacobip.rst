JacobiP
=======

`Jacobi polynomials <https://en.wikipedia.org/wiki/Jacobi_polynomials>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.polynomials.jacobi>`_, `WMA <https://reference.wolfram.com/language/ref/JacobiP.html>`_)


:code:`JacobiP` [:math:`n`, :math:`a`, :math:`b`, :math:`x`]
    returns the Jacobi polynomial :math:`P_n^{(a,b)}(x)`.





>>> JacobiP[1, a, b, z]
  = a / 2 - b / 2 + z (1 + a / 2 + b / 2)
>>> JacobiP[3.5 + I, 3, 2, 4 - I]
  = 1410.02 + 5797.3 I
