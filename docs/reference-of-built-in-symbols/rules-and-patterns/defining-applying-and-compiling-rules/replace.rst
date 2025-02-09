Replace
=======

`WMA link <https://reference.wolfram.com/language/ref/Replace.html>`_


:code:`Replace` [:math:`expr`, :math:`x` -> :math:`y`]
    yields the result of replacing :math:`expr` with :math:`y` if it         matches the pattern :math:`x`.

:code:`Replace` [:math:`expr`, :math:`x` -> :math:`y`, :math:`levelspec`]
    replaces only subexpressions at levels specified through         :math:`levelspec`.

:code:`Replace` [:math:`expr`, {:math:`x` -> :math:`y`, ...}]
    performs replacement with multiple rules, yielding a         single result expression.

:code:`Replace` [:math:`expr`, {{:math:`a` -> :math:`b`, ...}, {:math:`c` -> :math:`d`, ...}, ...}]
    returns a list containing the result of performing each         set of replacements.





>>> Replace[x, {x -> 2}]

    =
:math:`2`



By default, only the top level is searched for matches:

>>> Replace[1 + x, {x -> 2}]

    =
:math:`1+x`


>>> Replace[x, {{x -> 1}, {x -> 2}}]

    =
:math:`\left\{1,2\right\}`



Replace stops after the first replacement:

>>> Replace[x, {x -> {}, _List -> y}]

    =
:math:`\left\{\right\}`



Replace replaces the deepest levels first:

>>> Replace[x[1], {x[1] -> y, 1 -> 2}, All]

    =
:math:`x\left[2\right]`



By default, heads are not replaced:

>>> Replace[x[x[y]], x -> z, All]

    =
:math:`x\left[x\left[y\right]\right]`



Heads can be replaced using the :code:`Heads`  option:

>>> Replace[x[x[y]], x -> z, All, Heads -> True]

    =
:math:`z\left[z\left[y\right]\right]`



Note that heads are handled at the level of elements:

>>> Replace[x[x[y]], x -> z, {1}, Heads -> True]

    =
:math:`z\left[x\left[y\right]\right]`



You can use Replace as an operator:

>>> Replace[{x_ -> x + 1}][10]

    =
:math:`11`


