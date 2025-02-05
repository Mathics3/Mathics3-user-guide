RandomChoice
============

`WMA link <https://reference.wolfram.com/language/ref/RandomChoice.html>`_



:code:`RandomChoice` [:math:`items`]
    randomly picks one item from :math:`items`.

:code:`RandomChoice` [:math:`items`, :math:`n`]
    randomly picks :math:`n` items from :math:`items`. Each pick in the :math:`n` picks happens           from the given set of :math:`items`, so each item can be picked any number of times.

:code:`RandomChoice` [:math:`items`, {:math:`n_1`, :math:`n_2`, ...}]
    randomly picks items from :math:`items` and arranges the picked items in the           nested list structure described by {:math:`n_1`, :math:`n_2`, ...}.

:code:`RandomChoice` [:math:`weights` -> :math:`items`, :math:`n`]
    randomly picks :math:`n` items from :math:`items` and uses the corresponding numeric           values in :math:`weights` to determine how probable it is for each item in :math:`items`           to get picked (in the long run, items with higher weights will get picked           more often than ones with lower weight).

:code:`RandomChoice` [:math:`weights` -> :math:`items`]
    randomly picks one items from :math:`items` using weights :math:`weights`.

:code:`RandomChoice` [:math:`weights` -> :math:`items`, {:math:`n_1`, :math:`n_2`, ...}]
    randomly picks a structured list of items from :math:`items` using weights           :math:`weights`.





Note: :code:`SeedRandom`  is used below so we get repeatable "random" numbers that we     can test.

>>> SeedRandom[42]

>>> RandomChoice[{a, b, c}]
  = {c}
>>> SeedRandom[42] (* Set for repeatable randomness *)

>>> RandomChoice[{a, b, c}, 20]
  = {c, a, c, c, a, a, c, b, c, c, c, c, a, c, b, a, b, b, b, b}
>>> SeedRandom[42]

>>> RandomChoice[{"a", {1, 2}, x, {}}, 10]
  = {x, {}, a, x, x, {}, a, a, x, {1, 2}}
>>> SeedRandom[42]

>>> RandomChoice[{a, b, c}, {5, 2}]
  = {{c, a}, {c, c}, {a, a}, {c, b}, {c, c}}
>>> SeedRandom[42]

>>> RandomChoice[{1, 100, 5} -> {a, b, c}, 20]
  = {b, b, b, b, b, b, b, b, b, b, b, c, b, b, b, b, b, b, b, b}
