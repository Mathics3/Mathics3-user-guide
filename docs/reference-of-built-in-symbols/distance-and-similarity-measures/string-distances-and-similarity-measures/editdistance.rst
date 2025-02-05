EditDistance
============

`WMA link <https://reference.wolfram.com/language/ref/EditDistance.html>`_


:code:`EditDistance` [:math:`a`, :math:`b`]
    returns the Levenshtein distance of :math:`a` and :math:`b`, which is defined as the minimum number of
    insertions, deletions and substitutions on the constituents of :math:`a` and :math:`b` needed to transform
    one into the other.





>>> EditDistance["kitten", "kitchen"]
  = 2
>>> EditDistance["abc", "ac"]
  = 1
>>> EditDistance["abc", "acb"]
  = 2
>>> EditDistance["azbc", "abxyc"]
  = 3

The IgnoreCase option makes EditDistance ignore the case of letters:

>>> EditDistance["time", "Thyme"]
  = 3
>>> EditDistance["time", "Thyme", IgnoreCase -> True]
  = 2

EditDistance also works on lists:

>>> EditDistance[{1, E, 2, Pi}, {1, E, Pi, 2}]
  = 2
