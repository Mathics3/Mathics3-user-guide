Scoping
=======

By default, all symbols are "global" in \Mathics, i.e. they can be read and written in any part of your program.
However, sometimes "local" variables are needed in order not to disturb the global namespace. \Mathics provides two ways to support this:


- `<lexical scoping>`_ by :code:`Module` , and

- `<dynamic scoping>`_ by :code:`Block` .




:code:`Module` [{:math:`vars`}, :math:`expr`]
    localizes variables by giving them a temporary name of the form
    :code:`name$number` , where number is the current value of :code:`$ModuleNumber` . Each time a module
    is evaluated, :code:`$ModuleNumber`  is incremented.

:code:`Block` [{:math:`vars`}, :math:`expr`]
    temporarily stores the definitions of certain variables, evaluates
    :math:`expr` with reset values and restores the original definitions afterward.





Both scoping constructs shield inner variables from affecting outer ones:

>>> t = 3;


>>> Module[{t}, t = 2]
    =

:math:`2`


>>> Block[{t}, t = 2]
    =

:math:`2`


>>> t
    =

:math:`3`



:code:`Module`  creates new variables:

>>> y = x ^ 3;


>>> Module[{x = 2}, x * y]
    =

:math:`2 x^3`



:code:`Block`  does not:

>>> Block[{x = 2}, x * y]
    =

:math:`16`



Thus, :code:`Block`  can be used to temporarily assign a value to a variable:

>>> expr = x ^ 2 + x;


>>> Block[{x = 3}, expr]
    =

:math:`12`


>>> x
    =

:math:`x`



:code:`Block`  can also be used to temporarily change the value of system parameters:

>>> Block[{$RecursionLimit = 30}, x = 2 x]

    $RecursionLimit::reclim Recursion depth of 30 exceeded.
    =

:math:`\text{\$Aborted}`


>>> f[x_] := f[x + 1]; Block[{$IterationLimit = 30}, f[1]]

    $IterationLimit::itlim Iteration limit of 30 exceeded.
    =

:math:`\text{\$Aborted}`



It is common to use scoping constructs for function definitions with local variables:

>>> fac[n_] := Module[{k, p}, p = 1; For[k = 1, k <= n, ++k, p *= k]; p]


>>> fac[10]
    =

:math:`3628800`


>>> 10!
    =

:math:`3628800`


