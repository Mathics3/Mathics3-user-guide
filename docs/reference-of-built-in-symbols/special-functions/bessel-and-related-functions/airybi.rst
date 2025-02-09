AiryBi
======

`WMA link <https://reference.wolfram.com/language/ref/AiryBi.html>`_


:code:`AiryBi` [:math:`x`]
    returns the Airy function of the second kind :math:`Bi(x)`.





Exact values:

>>> AiryBi[0]

    =
:math:`\frac{3^{\frac{5}{6}}}{3 \text{Gamma}\left[\frac{2}{3}\right]}`



Numeric evaluation:

>>> AiryBi[0.5]

    =
:math:`0.854277`


>>> AiryBi[0.5 + I]

    =
:math:`0.688145+0.370815 I`


>>> Plot[AiryBi[x], {x, -10, 2}]

    =
.. image:: tmp8rb_d5pd.png
    :align: center



