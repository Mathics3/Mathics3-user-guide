ReplaceAll
==========

`WMA link <https://reference.wolfram.com/language/ref/ReplaceAll.html>`_


:code:`ReplaceAll` [:math:`expr`, :math:`x` -> :math:`y`]
    same as

:code:`:math:`expr` /. :math:`x` -> :math:`y``
    yields the result of replacing all subexpressions of         :math:`expr` matching the pattern :math:`x` with :math:`y`.

:code:`:math:`expr` /. {:math:`x` -> :math:`y`, ...}`
    performs replacement with multiple rules, yielding a         single result expression.

:code:`:math:`expr` /. {{:math:`a` -> :math:`b`, ...}, {:math:`c` -> :math:`d`, ...}, ...}`
    returns a list containing the result of performing each         set of replacements.





>>> a+b+c /. c->d
  = a + b + d
>>> g[a+b+c,a]/.g[x_+y_,x_]->{x,y}
  = {a, b + c}

If :math:`rules` is a list of lists, a list of all possible respective     replacements is returned:

>>> {a, b} /. {{a->x, b->y}, {a->u, b->v}}
  = {{x, y}, {u, v}}

The list can be arbitrarily nested:

>>> {a, b} /. {{{a->x, b->y}, {a->w, b->z}}, {a->u, b->v}}
  = {{{x, y}, {w, z}}, {u, v}}
>>> {a, b} /. {{{a->x, b->y}, a->w, b->z}, {a->u, b->v}}
  = {{a, b} /. {{a -> x, b -> y}, a -> w, b -> z}, {u, v}}

ReplaceAll also can be used as an operator:

>>> ReplaceAll[{a -> 1}][{a, b}]
  = {1, b}

ReplaceAll replaces the shallowest levels first:

>>> ReplaceAll[x[1], {x[1] -> y, 1 -> 2}]
  = y
