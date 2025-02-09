Erf
===

`Error function <https://en.wikipedia.org/wiki/Error_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.error_functions.erf>`_, `WMA <https://reference.wolfram.com/language/ref/Erf.html>`_)


:code:`Erf` [:math:`z`]
    returns the error function of :math:`z`.

:code:`Erf` [:math:`z_0`, :math:`z_1`]
    returns the result of :code:`Erf[:math:`z_1`] - Erf[:math:`z_0`]` .





:code:`Erf[:math:`x`]`  is an odd function:

>>> Erf[-x]

    =
:math:`-\text{Erf}\left[x\right]`


>>> Erf[1.0]

    =
:math:`0.842701`


>>> Erf[0]

    =
:math:`0`


>>> {Erf[0, x], Erf[x, 0]}

    =
:math:`\left\{\text{Erf}\left[x\right],-\text{Erf}\left[x\right]\right\}`


>>> Plot[Erf[x], {x, -2, 2}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_Erf_kcboz6m5.png
    :align: center



