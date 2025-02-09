Association
===========

`WMA link <https://reference.wolfram.com/language/ref/Association.html>`_


:code:`Association` [:math:`key_1` -> :math:`val_1`, :math:`key_2` -> :math:`val_2`, ...]
    same as

:code:`<|:math:`key_1` -> :math:`val_1`, :math:`key_2` -> :math:`val_2`, ...|>`
    represents an association between keys and values.





:code:`Association`  is the head of associations:

>>> Head[<|a -> x, b -> y, c -> z|>]

    =
:math:`\text{Association}`


>>> <|a -> x, b -> y|>

    =
:math:`\text{<$\vert$}a->x,b->y\text{$\vert$>}`


>>> Association[{a -> x, b -> y}]

    =
:math:`\text{<$\vert$}a->x,b->y\text{$\vert$>}`



Associations can be nested:

>>> <|a -> x, b -> y, <|a -> z, d -> t|>|>

    =
:math:`\text{<$\vert$}a->z,b->y,d->t\text{$\vert$>}`


