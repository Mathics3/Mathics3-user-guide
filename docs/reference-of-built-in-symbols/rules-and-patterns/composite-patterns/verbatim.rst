Verbatim
========

`WMA link <https://reference.wolfram.com/language/ref/Verbatim.html>`_


:code:`Verbatim` [:math:`expr`]
    prevents pattern constructs in :math:`expr` from taking effect,         allowing them to match themselves.





Create a pattern matching :code:`Blank` :

>>> _ /. Verbatim[_]->t

    =
:math:`t`


>>> x /. Verbatim[_]->t

    =
:math:`x`



Without :code:`Verbatim` , :code:`Blank`  has its normal effect:

>>> x /. _->t

    =
:math:`t`


