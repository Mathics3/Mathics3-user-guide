Dispatch
========

`WMA link <https://reference.wolfram.com/language/ref/Dispatch.html>`_


:code:`Dispatch` [:math:`rulelist`]
    Introduced for compatibility. Currently, it just return :math:`rulelist`.           In the future, it should return an optimized DispatchRules atom,           containing an optimized set of rules.





>>> rules = {{a_,b_}->a^b, {1,2}->3., F[x_]->x^2};


>>> F[2] /. rules

    =
:math:`4`


>>> dispatchrules = Dispatch[rules]

    =
:math:`\text{Dispatch}\left[\text{<3>}\right]`


>>> F[2] /. dispatchrules

    =
:math:`4`


