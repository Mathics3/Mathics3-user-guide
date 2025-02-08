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
    =

:math:`\begin{array}{l} a=2\end{array}`


>>> f[x_] := x ^ 2


>>> g[f] ^:= 2


>>> Definition[f]
    =

:math:`\begin{array}{l} f\left[\text{x\_}\right]=x^2\\ g\left[f\right]\text{${}^{\wedge}$=}2\end{array}`



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
    =

:math:`x\sim{}y\sim{}z`


>>> N[r]
    =

:math:`3.5`


>>> r[]
    =

:math:`\left\{2,3\right\}`


>>> r[5, Opt->7]
    =

:math:`\left\{5,7\right\}`



Its definition:

>>> Definition[r]
    =

:math:`\begin{array}{l} \text{Attributes}\left[r\right]=\left\{\text{Orderless}\right\}\\ \text{arg\_.}\sim{}\text{OptionsPattern}\left[r\right]=\left\{\text{arg},\text{OptionValue}\left[\text{Opt}\right]\right\}\\ N\left[r,\text{MachinePrecision}\right]=3.5\\ \text{Format}\left[\text{args\_\_\_},\text{MathMLForm}\right]=\text{Infix}\left[\left\{\text{args}\right\}, \text{\`{}\`{}$\sim$''}\right]\\ \text{Format}\left[\text{args\_\_\_},\text{OutputForm}\right]=\text{Infix}\left[\left\{\text{args}\right\}, \text{\`{}\`{}$\sim$''}\right]\\ \text{Format}\left[\text{args\_\_\_},\text{StandardForm}\right]=\text{Infix}\left[\left\{\text{args}\right\}, \text{\`{}\`{}$\sim$''}\right]\\ \text{Format}\left[\text{args\_\_\_},\text{TeXForm}\right]=\text{Infix}\left[\left\{\text{args}\right\}, \text{\`{}\`{}$\sim$''}\right]\\ \text{Format}\left[\text{args\_\_\_},\text{TraditionalForm}\right]=\text{Infix}\left[\left\{\text{args}\right\}, \text{\`{}\`{}$\sim$''}\right]\\ \text{Default}\left[r,1\right]=2\\ \text{Options}\left[r\right]=\left\{\text{Opt}->3\right\}\end{array}`



For :code:`ReadProtected`  symbols, :code:`Definition`  just prints attributes, default values and options:

>>> SetAttributes[r, ReadProtected]


>>> Definition[r]
    =

:math:`\begin{array}{l} \text{Attributes}\left[r\right]=\left\{\text{Orderless},\text{ReadProtected}\right\}\\ \text{Default}\left[r,1\right]=2\\ \text{Options}\left[r\right]=\left\{\text{Opt}->3\right\}\end{array}`



This is the same for built-in symbols:

>>> Definition[Plus]
    =

:math:`\begin{array}{l} \text{Attributes}\left[\text{Plus}\right]=\left\{\text{Flat},\text{Listable},\text{NumericFunction},\text{OneIdentity},\text{Orderless},\text{Protected}\right\}\\ \text{Default}\left[\text{Plus}\right]=0\end{array}`


>>> Definition[Level]
    =

:math:`\begin{array}{l} \text{Attributes}\left[\text{Level}\right]=\left\{\text{Protected}\right\}\\ \text{Options}\left[\text{Level}\right]=\left\{\text{Heads}->\text{False}\right\}\end{array}`



:code:`ReadProtected`  can be removed, unless the symbol is locked:

>>> ClearAttributes[r, ReadProtected]



:code:`Clear`  clears values:

>>> Clear[r]


>>> Definition[r]
    =

:math:`\begin{array}{l} \text{Attributes}\left[r\right]=\left\{\text{Orderless}\right\}\\ \text{Default}\left[r,1\right]=2\\ \text{Options}\left[r\right]=\left\{\text{Opt}->3\right\}\end{array}`



:code:`ClearAll`  clears everything:

>>> ClearAll[r]


>>> Definition[r]
    =

:math:`\text{Null}`



If a symbol is not defined at all, :code:`Null`  is printed:

>>> Definition[x]
    =

:math:`\text{Null}`


