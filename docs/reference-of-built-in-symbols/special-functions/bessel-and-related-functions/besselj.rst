BesselJ
=======

`Bessel function of the first kind <https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_first_kind:_J%CE%B1>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.besselj>`_, `WMA <https://reference.wolfram.com/language/ref/BesselJ.html>`_)


:code:`BesselJ` [:math:`n`, :math:`z`]
    returns the Bessel function of the first kind :math:`J_n(z)`.





>>> BesselJ[0, 5.2]
  = -0.11029
>>> D[BesselJ[n, z], z]
  = -BesselJ[1 + n, z] / 2 + BesselJ[-1 + n, z] / 2
>>> BesselJ[0., 0.]
  = 1.
>>> Plot[BesselJ[0, x], {x, 0, 10}]
  = -Graphics-

The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselJ[1/2, x]
  = Sqrt[2] Sin[x] / (Sqrt[x] Sqrt[Pi])

Some integrals can be expressed in terms of Bessel functions:

>>> Integrate[Cos[3 Sin[w]], {w, 0, Pi}]
  = Pi BesselJ[0, 3]
