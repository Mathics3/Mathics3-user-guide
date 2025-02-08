HoldPattern
===========

`WMA link <https://reference.wolfram.com/language/ref/HoldPattern.html>`_


:code:`HoldPattern` [:math:`expr`]
    is equivalent to :math:`expr` for pattern matching, but         maintains it in an unevaluated form.





>>> HoldPattern[x + x]
    =

:math:`\text{HoldPattern}\left[x+x\right]`


>>> x /. HoldPattern[x] -> t
    =

:math:`t`



:code:`HoldPattern`  has attribute :code:`HoldAll` :

>>> Attributes[HoldPattern]
    =

:math:`\left\{\text{HoldAll},\text{Protected}\right\}`


