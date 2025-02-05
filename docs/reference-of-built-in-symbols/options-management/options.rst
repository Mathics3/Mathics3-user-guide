Options
=======

`WMA link <https://reference.wolfram.com/language/ref/Options.html>`_


:code:`Options` [:math:`f`]
    gives a list of optional arguments to :math:`f` and their         default values.





You can assign values to :code:`Options`  to specify options.

>>> Options[f] = {n -> 2}
  = {n -> 2}
>>> Options[f]
  = {n :> 2}
>>> f[x_, OptionsPattern[f]] := x ^ OptionValue[n]

>>> f[x]
  = x ^ 2
>>> f[x, n -> 3]
  = x ^ 3

Delayed option rules are evaluated just when the corresponding :code:`OptionValue`  is called:

>>> f[a :> Print["value"]] /. f[OptionsPattern[{}]] :> (OptionValue[a]; Print["between"]; OptionValue[a]);


In contrast to that, normal option rules are evaluated immediately:

>>> f[a -> Print["value"]] /. f[OptionsPattern[{}]] :> (OptionValue[a]; Print["between"]; OptionValue[a]);


Options must be rules or delayed rules:

>>> Options[f] = {a}
  = {a}

A single rule need not be given inside a list:

>>> Options[f] = a -> b
  = a -> b
>>> Options[f]
  = {a :> b}

Options can only be assigned to symbols:

>>> Options[a + b] = {a -> b}
  = {a -> b}
