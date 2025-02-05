Definition
==========

`WMA link <https://reference.wolfram.com/language/ref/Definition.html>`_

:code:`Definition` [:math:`symbol`]
    prints as the definitions given for :math:`symbol`.
    This is in a form that can e stored in a package.





:code:`Definition`  does not print information for :code:`ReadProtected`  symbols.
:code:`Definition`  uses :code:`InputForm`  to format values.

>>> a = 2;

>>> Definition[a]
  = a = 2
>>> f[x_] := x ^ 2

>>> g[f] ^:= 2

>>> Definition[f]
  = f[x_] = x ^ 2
    
    g[f] ^= 2

Definition of a rather evolved (though meaningless) symbol:

>>> Attributes[r] := {Orderless}

>>> Format[r[args___]] := Infix[{args}, "~"]

>>> N[r] := 3.5

>>> Default[r, 1] := 2

>>> r::msg := "My message"

>>> Options[r] := {Opt -> 3}

>>> r[arg_., OptionsPattern[r]] := {arg, OptionValue[Opt]}


Some usage:

>>> r[z, x, y]
  = x ~ y ~ z
>>> N[r]
  = 3.5
>>> r[]
  = {2, 3}
>>> r[5, Opt->7]
  = {5, 7}

Its definition:

>>> Definition[r]
  = Attributes[r] = {Orderless}
    
    arg_. ~ OptionsPattern[r] = {arg, OptionValue[Opt]}
    
    N[r, MachinePrecision] = 3.5
    
    Format[args___, MathMLForm] = Infix[{args}, "~"]
    
    Format[args___, OutputForm] = Infix[{args}, "~"]
    
    Format[args___, StandardForm] = Infix[{args}, "~"]
    
    Format[args___, TeXForm] = Infix[{args}, "~"]
    
    Format[args___, TraditionalForm] = Infix[{args}, "~"]
    
    Default[r, 1] = 2
    
    Options[r] = {Opt -> 3}

For :code:`ReadProtected`  symbols, :code:`Definition`  just prints attributes, default values and options:

>>> SetAttributes[r, ReadProtected]

>>> Definition[r]
  = Attributes[r] = {Orderless, ReadProtected}
    
    Default[r, 1] = 2
    
    Options[r] = {Opt -> 3}

This is the same for built-in symbols:

>>> Definition[Plus]
  = Attributes[Plus] = {Flat, Listable, NumericFunction, OneIdentity, Orderless, Protected}
    
    Default[Plus] = 0
>>> Definition[Level]
  = Attributes[Level] = {Protected}
    
    Options[Level] = {Heads -> False}

:code:`ReadProtected`  can be removed, unless the symbol is locked:

>>> ClearAttributes[r, ReadProtected]


:code:`Clear`  clears values:

>>> Clear[r]

>>> Definition[r]
  = Attributes[r] = {Orderless}
    
    Default[r, 1] = 2
    
    Options[r] = {Opt -> 3}

:code:`ClearAll`  clears everything:

>>> ClearAll[r]

>>> Definition[r]
  = Null

If a symbol is not defined at all, :code:`Null`  is printed:

>>> Definition[x]
  = Null
