LaguerreL
=========

`Laguerre polynomials <https://en.wikipedia.org/wiki/Laguerre_polynomials>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.polynomials.leguarre_poly>`_, `WMA <https://reference.wolfram.com/language/ref/LeguerreL.html>`_)


:code:`LaguerreL` [:math:`n`, :math:`x`]
    returns the Laguerre polynomial :math:`L_n(x)`.

:code:`LaguerreL` [:math:`n`, :math:`a`, :math:`x`]
    returns the generalised Laguerre polynomial of order :math:`n`
    and index :math:`a`, :math:`L^a_n(x)`.





>>> LaguerreL[8, x]
    =

:math:`1-8 x+14 x^2-\frac{28 x^3}{3}+\frac{35 x^4}{12}-\frac{7 x^5}{15}+\frac{7 x^6}{180}-\frac{x^7}{630}+\frac{x^8}{40320}`


>>> LaguerreL[3/2, 1.7]
    =

:math:`-0.947134`


>>> LaguerreL[5, 2, x]
    =

:math:`21-35 x+\frac{35 x^2}{2}-\frac{7 x^3}{2}+\frac{7 x^4}{24}-\frac{x^5}{120}`


