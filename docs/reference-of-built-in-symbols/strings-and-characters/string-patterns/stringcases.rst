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
  = {axb}
>>> StringCases["axbaxxb", "a" ~~ x__ ~~ "b"]
  = {axbaxxb}
>>> StringCases["axbaxxb", Shortest["a" ~~ x__ ~~ "b"]]
  = {axb, axxb}
>>> StringCases["-abc- def -uvw- xyz", Shortest["-" ~~ x__ ~~ "-"] -> x]
  = {abc, uvw}
>>> StringCases["-öhi- -abc- -.-", "-" ~~ x : WordCharacter .. ~~ "-" -> x]
  = {öhi, abc}
>>> StringCases["abc-abc xyz-uvw", Shortest[x : WordCharacter .. ~~ "-" ~~ x_] -> x]
  = {abc}
>>> StringCases["abba", {"a" -> 10, "b" -> 20}, 2]
  = {10, 20}
>>> StringCases["a#ä_123", WordCharacter]
  = {a, ä, 1, 2, 3}
>>> StringCases["a#ä_123", LetterCharacter]
  = {a, ä}
