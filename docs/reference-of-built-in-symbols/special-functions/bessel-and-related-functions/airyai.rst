AiryAi
======

`Airy function of the first kind <https://en.wikipedia.org/wiki/Airy_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.airyai>`_, `WMA <https://reference.wolfram.com/language/ref/AiryAi.html>`_)

:code:`AiryAi` [:math:`x`]
    returns the Airy function :math:`Ai(x)`.





Exact values:

>>> AiryAi[0]

    =
:math:`\frac{3^{\frac{1}{3}}}{3 \text{Gamma}\left[\frac{2}{3}\right]}`



:code:`AiryAi`  can be evaluated numerically:

>>> AiryAi[0.5]

    =
:math:`0.231694`


>>> AiryAi[0.5 + I]

    =
:math:`0.157118-0.24104 I`


>>> Plot[AiryAi[x], {x, -10, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_AiryAi_uxy010is.png
    :align: center



