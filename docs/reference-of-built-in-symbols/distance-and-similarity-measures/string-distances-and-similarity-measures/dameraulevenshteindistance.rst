DamerauLevenshteinDistance
==========================

`WMA link <https://reference.wolfram.com/language/ref/DamerauLevenshteinDistance.html>`_


:code:`DamerauLevenshteinDistance` [:math:`a`, :math:`b`]
    returns the Damerau-Levenshtein distance of :math:`a` and :math:`b`, which is defined as the minimum number of
    transpositions, insertions, deletions and substitutions needed to transform one into the other.
    In contrast to EditDistance, DamerauLevenshteinDistance counts transposition of adjacent items (e.g.
    "ab" into "ba") as one operation of change.





>>> DamerauLevenshteinDistance["kitten", "kitchen"]

    =
:math:`2`


>>> DamerauLevenshteinDistance["abc", "ac"]

    =
:math:`1`


>>> DamerauLevenshteinDistance["abc", "acb"]

    =
:math:`1`


>>> DamerauLevenshteinDistance["azbc", "abxyc"]

    =
:math:`3`



The IgnoreCase option makes DamerauLevenshteinDistance ignore the case of letters:

>>> DamerauLevenshteinDistance["time", "Thyme"]

    =
:math:`3`


>>> DamerauLevenshteinDistance["time", "Thyme", IgnoreCase -> True]

    =
:math:`2`



DamerauLevenshteinDistance also works on lists:

>>> DamerauLevenshteinDistance[{1, E, 2, Pi}, {1, E, Pi, 2}]

    =
:math:`1`


