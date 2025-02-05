BesselY
=======

`Bessel function of the second kind <https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_second_kind:_Y%CE%B1>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.bessely>`_, `WMA <https://reference.wolfram.com/language/ref/BesselY.html>`_)


:code:`BesselY` [:math:`n`, :math:`z`]
    returns the Bessel function of the second kind :math:`Y_n(z)`.





>>> BesselY[1.5, 4]
  = 0.367112
>>> BesselY[0., 0.]
  = -Infinity
>>> Plot[BesselY[0, x], {x, 0, 10}]
  = -Graphics-

The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselY[-3/2, x]
  = Sqrt[2] Sqrt[x] (-Sin[x] / x ^ 2 + Cos[x] / x) / Sqrt[Pi]
>>> BesselY[0, 0]
  = -Infinity
