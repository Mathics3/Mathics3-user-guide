BesselK
=======

`Modified Bessel function of the second kind <https://en.wikipedia.org/wiki/Bessel_function#Modified_Bessel_functions:_I%CE%B1,_K%CE%B1>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.besselk>`_, `WMA <https://reference.wolfram.com/language/ref/BesselJ.html>`_)


:code:`BesselK` [:math:`n`, :math:`z`]
    returns the modified Bessel function of the second kind :math:`K_n(z)`.





>>> BesselK[1.5, 4]

    =
:math:`0.014347`


>>> Plot[BesselK[0, x], {x, 0, 5}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_BesselK_x9f8612w.png
    :align: center




The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselK[-3/2, x]

    =
:math:`\frac{\sqrt{2} \sqrt{x} \sqrt{ \pi } \left(\frac{E^{-x}}{x^2}+\frac{E^{-x}}{x}\right)}{2}`


