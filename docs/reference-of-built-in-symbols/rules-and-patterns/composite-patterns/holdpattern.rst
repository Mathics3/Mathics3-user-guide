HoldPattern
===========

`WMA link <https://reference.wolfram.com/language/ref/HoldPattern.html>`_


:code:`HoldPattern` [:math:`expr`]
    is equivalent to :math:`expr` for pattern matching, but         maintains it in an unevaluated form.





>>> HoldPattern[x + x]
  = HoldPattern[x + x]
>>> x /. HoldPattern[x] -> t
  = t

:code:`HoldPattern`  has attribute :code:`HoldAll` :

>>> Attributes[HoldPattern]
  = {HoldAll, Protected}
