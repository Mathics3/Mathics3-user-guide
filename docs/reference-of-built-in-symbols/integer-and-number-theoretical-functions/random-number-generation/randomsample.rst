RandomSample
============

`WMA link <https://reference.wolfram.com/language/ref/RandomSample.html>`_


:code:`RandomSample` [:math:`items`]
    randomly picks one item from :math:`items`.

:code:`RandomSample` [:math:`items`, :math:`n`]
    randomly picks :math:`n` items from :math:`items`. Each pick in the :math:`n` picks happens           after the previous items picked have been removed from :math:`items`, so each item           can be picked at most once.

:code:`RandomSample` [:math:`items`, {:math:`n_1`, :math:`n_2`, ...}]
    randomly picks items from :math:`items` and arranges the picked items in the           nested list structure described by {:math:`n_1`, :math:`n_2`, ...}.           Each item gets picked at most once.

:code:`RandomSample` [:math:`weights` -> :math:`items`, :math:`n`]
    randomly picks :math:`n` items from :math:`items` and uses the corresponding numeric           values in :math:`weights` to determine how probable it is for each item in :math:`items`           to get picked (in the long run, items with higher weights will get           picked more often than ones with lower weight). Each item gets picked at          most once.

:code:`RandomSample` [:math:`weights` -> :math:`items`]
    randomly picks one items from :math:`items` using weights :math:`weights`.           Each item gets picked at most once.

:code:`RandomSample` [:math:`weights` -> :math:`items`, {:math:`n_1`, :math:`n_2`, ...}]
    randomly picks a structured list of items from :math:`items` using weights :math:`weights`.
    Each item gets picked at most once.





>>> SeedRandom[42]

>>> RandomSample[{a, b, c, d}]
  = {b, d, a, c}
>>> SeedRandom[42]

>>> RandomSample[{a, b, c, d, e, f, g, h}, 7]
  = {b, f, a, h, c, e, d}
>>> SeedRandom[42]

>>> RandomSample[{"a", {1, 2}, x, {}}, 3]
  = {{1, 2}, {}, a}
>>> SeedRandom[42]

>>> RandomSample[Range[10]]
  = {9, 2, 6, 1, 8, 3, 10, 5, 4, 7}
>>> SeedRandom[42]

>>> RandomSample[Range[100], {2, 3}]
  = {{84, 54, 71}, {46, 45, 40}}
>>> SeedRandom[42]

>>> RandomSample[Range[100] -> Range[100], 5]
  = {62, 98, 86, 78, 40}
