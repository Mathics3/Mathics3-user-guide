BesselI
=======

`Modified Bessel function of the first kind <https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_first_kind:_J%CE%B1>`_ (`Sympy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.besseli>`_, `WMA <https://reference.wolfram.com/language/ref/BesselI.html>`_)


:code:`BesselI` [:math:`n`, :math:`z`]
    returns the modified Bessel function of the first kind :math:`I_n(z)`.





>>> BesselI[0, 0]
  = 1
>>> BesselI[1.5, 4]
  = 8.17263
>>> Plot[BesselI[0, x], {x, 0, 5}]
  = -Graphics-

The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselI[3/2, x]
  = Sqrt[2] Sqrt[x] (-Sinh[x] / x ^ 2 + Cosh[x] / x) / Sqrt[Pi]
