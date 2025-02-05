DamerauLevenshteinDistance
==========================

`WMA link <https://reference.wolfram.com/language/ref/DamerauLevenshteinDistance.html>`_


:code:`DamerauLevenshteinDistance` [:math:`a`, :math:`b`]
    returns the Damerau-Levenshtein distance of :math:`a` and :math:`b`, which is defined as the minimum number of
    transpositions, insertions, deletions and substitutions needed to transform one into the other.
    In contrast to EditDistance, DamerauLevenshteinDistance counts transposition of adjacent items (e.g.
    "ab" into "ba") as one operation of change.





>>> DamerauLevenshteinDistance["kitten", "kitchen"]
  = 2
>>> DamerauLevenshteinDistance["abc", "ac"]
  = 1
>>> DamerauLevenshteinDistance["abc", "acb"]
  = 1
>>> DamerauLevenshteinDistance["azbc", "abxyc"]
  = 3

The IgnoreCase option makes DamerauLevenshteinDistance ignore the case of letters:

>>> DamerauLevenshteinDistance["time", "Thyme"]
  = 3
>>> DamerauLevenshteinDistance["time", "Thyme", IgnoreCase -> True]
  = 2

DamerauLevenshteinDistance also works on lists:

>>> DamerauLevenshteinDistance[{1, E, 2, Pi}, {1, E, Pi, 2}]
  = 1
