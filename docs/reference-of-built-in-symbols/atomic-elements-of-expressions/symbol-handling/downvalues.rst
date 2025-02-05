DownValues
==========

`WMA link <https://reference.wolfram.com/language/ref/DownValues.html>`_

:code:`DownValues` [:math:`symbol`]
    gives the list of downvalues associated with :math:`symbol`.





:code:`DownValues`  uses :code:`HoldPattern`  and :code:`RuleDelayed`  to protect the     downvalues from being evaluated, and it has attribute     :code:`HoldAll`  to get the specified symbol instead of its value.

>>> f[x_] := x ^ 2

>>> DownValues[f]
  = {HoldPattern[f[x_]] :> x ^ 2}

Mathics will sort the rules you assign to a symbol according to     their specificity. If it cannot decide which rule is more special,     the newer one will get higher precedence.

>>> f[x_Integer] := 2

>>> f[x_Real] := 3

>>> DownValues[f]
  = {HoldPattern[f[x_Real]] :> 3, HoldPattern[f[x_Integer]] :> 2, HoldPattern[f[x_]] :> x ^ 2}
>>> f[3]
  = 2
>>> f[3.]
  = 3
>>> f[a]
  = a ^ 2

The default order of patterns can be computed using :code:`Sort`  with     :code:`PatternsOrderedQ` :

>>> Sort[{x_, x_Integer}, PatternsOrderedQ]
  = {x_Integer, x_}

By assigning values to :code:`DownValues` , you can override the default     ordering:

>>> DownValues[g] := {g[x_] :> x ^ 2, g[x_Integer] :> x}

>>> g[2]
  = 4

Fibonacci numbers:

>>> DownValues[fib] := {fib[0] -> 0, fib[1] -> 1, fib[n_] :> fib[n - 1] + fib[n - 2]}

>>> fib[5]
  = 5
