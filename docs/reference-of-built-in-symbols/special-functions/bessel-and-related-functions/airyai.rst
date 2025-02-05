AiryAi
======

`Airy function of the first kind <https://en.wikipedia.org/wiki/Airy_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.bessel.airyai>`_, `WMA <https://reference.wolfram.com/language/ref/AiryAi.html>`_)

:code:`AiryAi` [:math:`x`]
    returns the Airy function :math:`Ai(x)`.





Exact values:

>>> AiryAi[0]
  = 3 ^ (1 / 3) / (3 Gamma[2 / 3])

:code:`AiryAi`  can be evaluated numerically:

>>> AiryAi[0.5]
  = 0.231694
>>> AiryAi[0.5 + I]
  = 0.157118 - 0.24104 I
>>> Plot[AiryAi[x], {x, -10, 10}]
  = -Graphics-
