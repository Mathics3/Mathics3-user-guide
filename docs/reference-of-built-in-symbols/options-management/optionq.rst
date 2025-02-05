OptionQ
=======

`WMA link <https://reference.wolfram.com/language/ref/OptionQ.html>`_


:code:`OptionQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` has the form of a valid option          specification.





Examples of option specifications:

>>> OptionQ[a -> True]
  = True
>>> OptionQ[a :> True]
  = True
>>> OptionQ[{a -> True}]
  = True
>>> OptionQ[{a :> True}]
  = True

Options lists are flattened when are applied, so

>>> OptionQ[{a -> True, {b->1, "c"->2}}]
  = True
>>> OptionQ[{a -> True, {b->1, c}}]
  = False
>>> OptionQ[{a -> True, F[b->1,c->2]}]
  = False

:code:`OptionQ`  returns :code:`False`  if its argument is not a valid option
specification:

>>> OptionQ[x]
  = False
