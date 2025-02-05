AiryBi
======

`WMA link <https://reference.wolfram.com/language/ref/AiryBi.html>`_


:code:`AiryBi` [:math:`x`]
    returns the Airy function of the second kind :math:`Bi(x)`.





Exact values:

>>> AiryBi[0]
  = 3 ^ (5 / 6) / (3 Gamma[2 / 3])

Numeric evaluation:

>>> AiryBi[0.5]
  = 0.854277
>>> AiryBi[0.5 + I]
  = 0.688145 + 0.370815 I
>>> Plot[AiryBi[x], {x, -10, 2}]
  = -Graphics-
