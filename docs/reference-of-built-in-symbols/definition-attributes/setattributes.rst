SetAttributes
=============

`WMA link <https://reference.wolfram.com/language/ref/SetAttributes.html>`_


:code:`SetAttributes` [:math:`symbol`, :math:`attrib`]
    adds :math:`attrib` to the list of :math:`symbol`'s attributes.





>>> SetAttributes[f, Flat]


>>> Attributes[f]
    =

:math:`\left\{\text{Flat}\right\}`



Multiple attributes can be set at the same time using lists:

>>> SetAttributes[{f, g}, {Flat, Orderless}]


>>> Attributes[g]
    =

:math:`\left\{\text{Flat},\text{Orderless}\right\}`


