Options
=======

`WMA link <https://reference.wolfram.com/language/ref/Options.html>`_


:code:`Options` [:math:`f`]
    gives a list of optional arguments to :math:`f` and their         default values.





You can assign values to :code:`Options`  to specify options.

>>> Options[f] = {n -> 2}
    =

:math:`\left\{n->2\right\}`


>>> Options[f]
    =

:math:`\left\{n\text{:>}2\right\}`


>>> f[x_, OptionsPattern[f]] := x ^ OptionValue[n]


>>> f[x]
    =

:math:`x^2`


>>> f[x, n -> 3]
    =

:math:`x^3`



Delayed option rules are evaluated just when the corresponding :code:`OptionValue`  is called:

>>> f[a :> Print["value"]] /. f[OptionsPattern[{}]] :> (OptionValue[a]; Print["between"]; OptionValue[a]);

    value

    between

    value



In contrast to that, normal option rules are evaluated immediately:

>>> f[a -> Print["value"]] /. f[OptionsPattern[{}]] :> (OptionValue[a]; Print["between"]; OptionValue[a]);

    value

    between



Options must be rules or delayed rules:

>>> Options[f] = {a}

    Options::options {a} is not a valid list of option rules.
    =

:math:`\left\{a\right\}`



A single rule need not be given inside a list:

>>> Options[f] = a -> b
    =

:math:`a->b`


>>> Options[f]
    =

:math:`\left\{a\text{:>}b\right\}`



Options can only be assigned to symbols:

>>> Options[a + b] = {a -> b}

    Options::sym Argument a + b at position 1 is expected to be a symbol.
    =

:math:`\left\{a->b\right\}`


