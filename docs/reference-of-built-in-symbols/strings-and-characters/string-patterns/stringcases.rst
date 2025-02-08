StringCases
===========

`WMA link <https://reference.wolfram.com/language/ref/StringCases.html>`_


:code:`StringCases` [":math:`string`", :math:`pattern`]
    gives all occurrences of :math:`pattern` in :math:`string`.

:code:`StringReplace` [":math:`string`", :math:`pattern` -> :math:`form`]
    gives all instances of :math:`form` that stem from occurrences of :math:`pattern` in :math:`string`.

:code:`StringCases` [":math:`string`", {:math:`pattern_1`, :math:`pattern_2`, ...}]
    gives all occurrences of :math:`pattern_1`, :math:`pattern_2`, ....

:code:`StringReplace` [":math:`string`", :math:`pattern`, :math:`n`]
    gives only the first :math:`n` occurrences.

:code:`StringReplace` [{":math:`string_1`", ":math:`string_2`", ...}, :math:`pattern`]
    gives occurrences in :math:`string_1`, :math:`string_2`, ...





>>> StringCases["axbaxxb", "a" ~~ x_ ~~ "b"]
    =

:math:`\left\{\text{axb}\right\}`


>>> StringCases["axbaxxb", "a" ~~ x__ ~~ "b"]
    =

:math:`\left\{\text{axbaxxb}\right\}`


>>> StringCases["axbaxxb", Shortest["a" ~~ x__ ~~ "b"]]
    =

:math:`\left\{\text{axb},\text{axxb}\right\}`


>>> StringCases["-abc- def -uvw- xyz", Shortest["-" ~~ x__ ~~ "-"] -> x]
    =

:math:`\left\{\text{abc},\text{uvw}\right\}`


>>> StringCases["-öhi- -abc- -.-", "-" ~~ x : WordCharacter .. ~~ "-" -> x]
    =

:math:`\left\{\text{öhi},\text{abc}\right\}`


>>> StringCases["abc-abc xyz-uvw", Shortest[x : WordCharacter .. ~~ "-" ~~ x_] -> x]
    =

:math:`\left\{\text{abc}\right\}`


>>> StringCases["abba", {"a" -> 10, "b" -> 20}, 2]
    =

:math:`\left\{10,20\right\}`


>>> StringCases["a#ä_123", WordCharacter]
    =

:math:`\left\{\text{a},\text{ä},\text{1},\text{2},\text{3}\right\}`


>>> StringCases["a#ä_123", LetterCharacter]
    =

:math:`\left\{\text{a},\text{ä}\right\}`


