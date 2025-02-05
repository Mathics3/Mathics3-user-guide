Dispatch
========

`WMA link <https://reference.wolfram.com/language/ref/DispatchAtom.html>`_


:code:`Dispatch` [:math:`rulelist`]
    Introduced for compatibility. Currently, it just return :math:`rulelist`.           In the future, it should return an optimized DispatchRules atom,           containing an optimized set of rules.





>>> rules = {{a_,b_}->a^b, {1,2}->3., F[x_]->x^2};

>>> F[2] /. rules
  = 4
>>> dispatchrules = Dispatch[rules]
  = Dispatch[<3>]
>>> F[2] /. dispatchrules
  = 4
