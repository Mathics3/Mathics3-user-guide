MapApply
========

`WMA link <https://reference.wolfram.com/language/ref/MapApply.html>`_


:code:`MapApply` [:math:`f`, :math:`expr`]
    same as

:code:`:math:`f` @@@ :math:`expr``
    is equivalent to :code:`Apply[:math:`f`, :math:`expr`, {1}]` .





>>> f @@@ {{a, b}, {c, d}}

    =
:math:`\left\{f\left[a,b\right],f\left[c,d\right]\right\}`


