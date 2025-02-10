Gamma
=====

`Gamma function <https://en.wikipedia.org/wiki/Gamma_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#module-sympy.functions.special.gamma_functions>`_, `mpmath <https://mpmath.org/doc/current/functions/gamma.html#gamma>`_, `WMA <https://reference.wolfram.com/language/ref/Gamma.html>`_)

The gamma function is one commonly used extension of the factorial function     applied to complex numbers, and is defined for all complex numbers except     the non-positive integers.


:code:`Gamma` [:math:`z`]
    is the gamma function on the complex number :math:`z`.

:code:`Gamma` [:math:`z`, :math:`x`]
    is the upper incomplete gamma function.

:code:`Gamma` [:math:`z`, :math:`x_0`, :math:`x_1`]
    is equivalent to :code:`Gamma[:math:`z`, :math:`x_0`] - Gamma[:math:`z`, :math:`x_1`]` .





:code:`Gamma[:math:`z`]`  is equivalent to :code:`(:math:`z` - 1)!` :

>>> Simplify[Gamma[z] - (z - 1)!]

    =
:math:`0`



Exact arguments:

>>> Gamma[8]

    =
:math:`5040`


>>> Gamma[1/2]

    =
:math:`\sqrt{ \pi }`


>>> Gamma[1, x]

    =
:math:`E^{-x}`


>>> Gamma[0, x]

    =
:math:`\text{ExpIntegralE}\left[1,x\right]`



Numeric arguments:

>>> Gamma[123.78]

    =
:math:`4.21078\text{*${}^{\wedge}$}204`


>>> Gamma[1. + I]

    =
:math:`0.498016-0.15495 I`



Both :code:`Gamma`  and :code:`Factorial`  functions are continuous:

>>> Plot[{Gamma[x], x!}, {x, 0, 4}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_Gamma_1i_6g0ol.png
    :align: center



