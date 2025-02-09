LegendreP
=========

`Lengendre polynomials <https://en.wikipedia.org/wiki/Legendre_polynomials>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.polynomials.legendre>`_, `WMA <https://reference.wolfram.com/language/ref/LegendreP>`_)

:code:`LegendreP` [:math:`n`, :math:`x`]
    returns the Legendre polynomial :math:`P_n(x)`.

:code:`LegendreP` [:math:`n`, :math:`m`, :math:`x`]
    returns the associated Legendre polynomial :math:`P^m_n(x)`.





>>> LegendreP[4, x]

    =
:math:`\frac{3}{8}-\frac{15 x^2}{4}+\frac{35 x^4}{8}`


>>> LegendreP[5/2, 1.5]

    =
:math:`4.17762`


>>> LegendreP[1.75, 1.4, 0.53]

    =
:math:`-1.32619`


>>> LegendreP[1.6, 3.1, 1.5]

    =
:math:`-0.303998-1.91937 I`



:code:`LegendreP`  can be used to draw generalized Lissajous figures:

>>> ParametricPlot[ {LegendreP[7, x], LegendreP[5, x]}, {x, -1, 1}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_LegendreP_wvj0ndqn.png
    :align: center



