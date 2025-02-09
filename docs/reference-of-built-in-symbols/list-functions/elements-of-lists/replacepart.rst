ReplacePart
===========

`WMA link <https://reference.wolfram.com/language/ref/ReplacePart.html>`_


:code:`ReplacePart` [:math:`expr`, :math:`i` -> :math:`new`]
    replaces part :math:`i` in :math:`expr` with :math:`new`.

:code:`ReplacePart` [:math:`expr`, {{:math:`i`, :math:`j`} -> :math:`e_1`, {:math:`k`, :math:`l`} -> :math:`e_2`}]
    replaces parts :math:`i` and :math:`j` with :math:`e_1`, and parts :math:`k` and :math:`l` with :math:`e_2`.





>>> ReplacePart[{a, b, c}, 1 -> t]

    =
:math:`\left\{t,b,c\right\}`


>>> ReplacePart[{{a, b}, {c, d}}, {2, 1} -> t]

    =
:math:`\left\{\left\{a,b\right\},\left\{t,d\right\}\right\}`


>>> ReplacePart[{{a, b}, {c, d}}, {{2, 1} -> t, {1, 1} -> t}]

    =
:math:`\left\{\left\{t,b\right\},\left\{t,d\right\}\right\}`


>>> ReplacePart[{a, b, c}, {{1}, {2}} -> t]

    =
:math:`\left\{t,t,c\right\}`



Delayed rules are evaluated once for each replacement:

>>> n = 1;


>>> ReplacePart[{a, b, c, d}, {{1}, {3}} :> n++]

    =
:math:`\left\{1,b,2,d\right\}`



Non-existing parts are simply ignored:

>>> ReplacePart[{a, b, c}, 4 -> t]

    =
:math:`\left\{a,b,c\right\}`



You can replace heads by replacing part 0:

>>> ReplacePart[{a, b, c}, 0 -> Times]

    =
:math:`a b c`



(This is equivalent to :code:`Apply` .)

Negative part numbers count from the end:

>>> ReplacePart[{a, b, c}, -1 -> t]

    =
:math:`\left\{a,b,t\right\}`


