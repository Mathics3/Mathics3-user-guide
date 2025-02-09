BesselY
=======

`Bessel function of the second kind <https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_second_kind:_Y%CE%B1>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.bessely>`_, `WMA <https://reference.wolfram.com/language/ref/BesselY.html>`_)


:code:`BesselY` [:math:`n`, :math:`z`]
    returns the Bessel function of the second kind :math:`Y_n(z)`.





>>> BesselY[1.5, 4]

    =
:math:`0.367112`


>>> BesselY[0., 0.]

    =
:math:`-\infty`


>>> Plot[BesselY[0, x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_BesselY_zveyg6ml.png
    :align: center




The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselY[-3/2, x]

    =
:math:`\frac{\sqrt{2} \sqrt{x} \left(-\frac{\text{Sin}\left[x\right]}{x^2}+\frac{\text{Cos}\left[x\right]}{x}\right)}{\sqrt{ \pi }}`


>>> BesselY[0, 0]

    =
:math:`-\infty`


