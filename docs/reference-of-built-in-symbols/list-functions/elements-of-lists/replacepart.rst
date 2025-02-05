ReplacePart
===========

`WMA link <https://reference.wolfram.com/language/ref/ReplacePart.html>`_


:code:`ReplacePart` [:math:`expr`, :math:`i` -> :math:`new`]
    replaces part :math:`i` in :math:`expr` with :math:`new`.

:code:`ReplacePart` [:math:`expr`, {{:math:`i`, :math:`j`} -> :math:`e_1`, {:math:`k`, :math:`l`} -> :math:`e_2`}]
    replaces parts :math:`i` and :math:`j` with :math:`e_1`, and parts :math:`k` and :math:`l` with :math:`e_2`.





>>> ReplacePart[{a, b, c}, 1 -> t]
  = {t, b, c}
>>> ReplacePart[{{a, b}, {c, d}}, {2, 1} -> t]
  = {{a, b}, {t, d}}
>>> ReplacePart[{{a, b}, {c, d}}, {{2, 1} -> t, {1, 1} -> t}]
  = {{t, b}, {t, d}}
>>> ReplacePart[{a, b, c}, {{1}, {2}} -> t]
  = {t, t, c}

Delayed rules are evaluated once for each replacement:

>>> n = 1;

>>> ReplacePart[{a, b, c, d}, {{1}, {3}} :> n++]
  = {1, b, 2, d}

Non-existing parts are simply ignored:

>>> ReplacePart[{a, b, c}, 4 -> t]
  = {a, b, c}

You can replace heads by replacing part 0:

>>> ReplacePart[{a, b, c}, 0 -> Times]
  = a b c

(This is equivalent to :code:`Apply` .)

Negative part numbers count from the end:

>>> ReplacePart[{a, b, c}, -1 -> t]
  = {a, b, t}
