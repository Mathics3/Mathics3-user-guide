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
  = 2

By default, only the top level is searched for matches:

>>> Replace[1 + x, {x -> 2}]
  = 1 + x
>>> Replace[x, {{x -> 1}, {x -> 2}}]
  = {1, 2}

Replace stops after the first replacement:

>>> Replace[x, {x -> {}, _List -> y}]
  = {}

Replace replaces the deepest levels first:

>>> Replace[x[1], {x[1] -> y, 1 -> 2}, All]
  = x[2]

By default, heads are not replaced:

>>> Replace[x[x[y]], x -> z, All]
  = x[x[y]]

Heads can be replaced using the :code:`Heads`  option:

>>> Replace[x[x[y]], x -> z, All, Heads -> True]
  = z[z[y]]

Note that heads are handled at the level of elements:

>>> Replace[x[x[y]], x -> z, {1}, Heads -> True]
  = z[x[y]]

You can use Replace as an operator:

>>> Replace[{x_ -> x + 1}][10]
  = 11
