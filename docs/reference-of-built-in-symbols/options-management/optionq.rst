OptionQ
=======

`WMA link <https://reference.wolfram.com/language/ref/OptionQ.html>`_


:code:`OptionQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` has the form of a valid option          specification.





Examples of option specifications:

>>> OptionQ[a -> True]

    =
:math:`\text{True}`


>>> OptionQ[a :> True]

    =
:math:`\text{True}`


>>> OptionQ[{a -> True}]

    =
:math:`\text{True}`


>>> OptionQ[{a :> True}]

    =
:math:`\text{True}`



Options lists are flattened when are applied, so

>>> OptionQ[{a -> True, {b->1, "c"->2}}]

    =
:math:`\text{True}`


>>> OptionQ[{a -> True, {b->1, c}}]

    =
:math:`\text{False}`


>>> OptionQ[{a -> True, F[b->1,c->2]}]

    =
:math:`\text{False}`



:code:`OptionQ`  returns :code:`False`  if its argument is not a valid option
specification:

>>> OptionQ[x]

    =
:math:`\text{False}`


