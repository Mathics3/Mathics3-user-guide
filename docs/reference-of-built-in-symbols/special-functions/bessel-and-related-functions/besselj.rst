BesselJ
=======

`Bessel function of the first kind <https://en.wikipedia.org/wiki/Bessel_function#Bessel_functions_of_the_first_kind:_J%CE%B1>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.besselj>`_, `WMA <https://reference.wolfram.com/language/ref/BesselJ.html>`_)


:code:`BesselJ` [:math:`n`, :math:`z`]
    returns the Bessel function of the first kind :math:`J_n(z)`.





>>> BesselJ[0, 5.2]

    =
:math:`-0.11029`


>>> D[BesselJ[n, z], z]

    =
:math:`-\frac{\text{BesselJ}\left[1+n,z\right]}{2}+\frac{\text{BesselJ}\left[-1+n,z\right]}{2}`


>>> BesselJ[0., 0.]

    =
:math:`1.`


>>> Plot[BesselJ[0, x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_BesselJ_ur0b4evh.png
    :align: center




The special case of half-integer index is expanded using Rayleigh's formulas:

>>> BesselJ[1/2, x]

    =
:math:`\frac{\sqrt{2} \text{Sin}\left[x\right]}{\sqrt{x} \sqrt{ \pi }}`



Some integrals can be expressed in terms of Bessel functions:

>>> Integrate[Cos[3 Sin[w]], {w, 0, Pi}]

    =
:math:`\pi  \text{BesselJ}\left[0,3\right]`


